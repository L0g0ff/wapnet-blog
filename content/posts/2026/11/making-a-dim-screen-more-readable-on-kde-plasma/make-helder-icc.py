#!/usr/bin/env python3
"""Generate ICC v2 RGB display profiles with sRGB primaries and raised gamma.

These intentionally inaccurate profiles lift midtones through KWin color
management. They do not increase the backlight or calibrate the display.
"""
import struct, os

def s15(x): return struct.pack('>i', round(x * 65536))
def pad4(b): return b + b'\0' * (-len(b) % 4)

def xyz(x, y, z): return b'XYZ ' + b'\0'*4 + s15(x) + s15(y) + s15(z)
def curv(g):      return b'curv' + b'\0'*4 + struct.pack('>IH', 1, round(g * 256))
def text(s):      return b'text' + b'\0'*4 + s.encode() + b'\0'
def desc(s):
    a = s.encode() + b'\0'
    return (b'desc' + b'\0'*4 + struct.pack('>I', len(a)) + a +
            struct.pack('>II', 0, 0) + struct.pack('>HB', 0, 0) + b'\0'*67)

def profile(name, gamma):
    D50 = (0.9642, 1.0, 0.8249)
    tags = [
        (b'desc', desc(name)),
        (b'cprt', text('No copyright, use freely')),
        (b'wtpt', xyz(*D50)),
        (b'rXYZ', xyz(0.4361, 0.2225, 0.0139)),
        (b'gXYZ', xyz(0.3851, 0.7169, 0.0971)),
        (b'bXYZ', xyz(0.1431, 0.0606, 0.7141)),
        (b'rTRC', curv(gamma)),
        (b'gTRC', curv(gamma)),
        (b'bTRC', curv(gamma)),
    ]
    off = 128 + 4 + 12 * len(tags)
    table, data = b'', b''
    for sig, body in tags:
        table += sig + struct.pack('>II', off + len(data), len(body))
        data += pad4(body)
    body = struct.pack('>I', len(tags)) + table + data
    size = 128 + len(body)
    hdr = (struct.pack('>I', size) + b'\0'*4 + struct.pack('>I', 0x02100000) +
           b'mntrRGB XYZ ' + struct.pack('>6H', 2026, 11, 7, 0, 0, 0) +
           b'acsp' + b'\0'*4 + struct.pack('>I', 0) + b'\0'*8 + b'\0'*8 +
           struct.pack('>I', 0) + s15(D50[0]) + s15(D50[1]) + s15(D50[2]) +
           b'\0'*4 + b'\0'*16 + b'\0'*28)
    assert len(hdr) == 128
    return hdr + body

out = os.path.dirname(os.path.abspath(__file__))
for lvl, g in {1: 2.6, 2: 3.0, 3: 3.4}.items():
    p = os.path.join(out, f'helder-{lvl}.icc')
    open(p, 'wb').write(profile(f'Helder {lvl} (sRGB, gamma {g})', g))
    print(p, f'gamma {g} -> effective ~in^{2.2/g:.2f}')
