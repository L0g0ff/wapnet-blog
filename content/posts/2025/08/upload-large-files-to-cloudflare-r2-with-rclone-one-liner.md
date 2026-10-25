---
author: thomasf
categories:
  - linux
  - networking
date: "2025-08-19T14:45:44+00:00"
guid: https://blog.wapnet.nl/?p=2248
parent_post_id: null
post_id: "2248"
title: Upload Large Files to Cloudflare R2 with rclone (One-liner)
url: /2025/08/upload-large-files-to-cloudflare-r2-with-rclone-one-liner/

cover:
  image: /images/covers/upload-large-files-to-cloudflare-r2-with-rclone-one-liner.jpg
  alt: Large file split into chunks uploading in parallel from a terminal to a cloud bucket
---
I have a custom operating system with the name KompassOS ([www.kompassos.nl](http://www.kompassos.nl)) and sometimes we need to upload big ISO files to cloudflare. But if the files all the files bigger than 300MB you have to upload with the S3 API.

So Need to upload large files (>300MB) to Cloudflare R2? Here's how to do it with a single rclone command without creating config files.

## Prerequisites

1. **Create an R2 bucket** in your Cloudflare dashboard
1. **Generate API credentials** in Cloudflare R2 → Manage R2 API Tokens
1. **Install rclone**

## The Command

```
rclone copy ./your-file.iso ':s3,provider=Cloudflare,access_key_id=YOUR_ACCESS_KEY,secret_access_key=YOUR_SECRET_KEY,endpoint=YOUR_ACCOUNT_ID.r2.cloudflarestorage.com,no_check_bucket=true,force_path_style=true:your-bucket/'

```

## Key Parameters

- `provider=Cloudflare` \- Tells rclone to use R2-specific settings
- `no_check_bucket=true` \- Prevents bucket creation attempts (avoids 403 errors)
- `force_path_style=true` \- Ensures compatibility with R2's API
- Replace `YOUR_ACCOUNT_ID` with your Cloudflare account ID
- Replace `YOUR_ACCESS_KEY` and `YOUR_SECRET_KEY` with your R2 credentials
- Replace `your-bucket` with your bucket name

## Why This Works

Regular file uploads in web interfaces are limited to 300MB. This method uses rclone's multipart upload capability, allowing files of any size to be uploaded directly to R2 storage.

Perfect for ISOs, backups, and other large files!

Happy uploading :)
