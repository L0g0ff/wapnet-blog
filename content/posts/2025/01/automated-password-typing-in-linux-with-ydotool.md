---
author: thomasf
categories:
  - linux
date: "2025-01-16T21:38:45+00:00"
guid: https://blog.wapnet.nl/?p=2226
parent_post_id: null
post_id: "2226"
title: Automated Password Typing in Linux with ydotool
url: /2025/01/automated-password-typing-in-linux-with-ydotool/

---
When working with remote desktop sessions in Linux, especially nested ones (like RDP inside Citrix), typing passwords can be challenging. Special characters and capital letters often don't transmit correctly, leading to frustrating login attempts. This guide presents a robust solution using ydotool that handles all password characters correctly, even in nested remote sessions.

## The Challenge

Common issues when typing passwords in remote sessions include:

- Shift key states not being properly recognized
- Special characters getting mangled
- Inconsistent behavior with capital letters
- Characters being dropped or misinterpreted

## The Solution

Our solution uses `ydotool`, a modern input automation tool for Wayland. The script we've developed handles every possible password character correctly by:

- Explicitly defining which characters need shift
- Processing input character by character
- Adding small delays to ensure reliability
- Resetting modifier keys before starting

Here's the complete script (in txt otherwise it breaks this CMS ;))

[auto-type-script](/wp-content/uploads/2025/01/auto-type-script.txt) [Download](/wp-content/uploads/2025/01/auto-type-script.txt)

## How It Works

Let's break down the script:

1. **Initial Setup**
   - `sleep 2s`: Gives you time to focus the correct window
   - `ydotool key 42:0 54:0 29:0 97:0`: Resets all modifier keys (left/right shift and ctrl)
1. **Character Sets**
   - `NO_SHIFT_CHARS`: Defines all characters that don't require shift
   - `SHIFT_CHARS`: Defines all characters that do require shift
1. **Input Processing**
   - `wl-paste`: Gets text from clipboard
   - `grep -o .`: Splits into individual characters
   - `while IFS= read -r char`: Processes each character while preserving whitespace
1. **Character Handling**
   - For shift characters:
     1. Press shift
     1. Type character
     1. Release shift
     1. Small delay between actions
   - For non-shift characters:
     1. Type character directly
     1. Small delay after

## Usage

1. Copy your password to the clipboard
1. Run the script
1. Click in the password field within 2 seconds
1. Watch as your password is typed perfectly, character by character

## Why This Works

This approach is superior to simple clipboard pasting or basic automation because:

- It handles every character explicitly and correctly
- The small delays ensure reliable transmission in nested sessions
- The modifier key reset prevents state issues
- It works consistently across different remote desktop setups

## Requirements

- Linux with Wayland
- ydotool installed
- wl-clipboard installed

## Security Considerations

While this script makes password entry more reliable, remember:

- Clear your clipboard after use
- Don't store the script with your actual passwords
- Be aware of your surroundings when using it

## Common Use Cases

This solution is particularly useful for:

- Complex passwords in nested remote sessions
- Environments where clipboard paste is disabled
- Situations requiring reliable special character input
- Multiple remote desktop layers

## Conclusion

This script provides a reliable solution for password typing in Linux, especially in complex remote desktop scenarios. By explicitly handling each character type and adding appropriate delays, it ensures consistent and correct password entry every time.

Happy type ehh pasting ;-)
