# re_upload

## RealEarth™ Upload

### Upload Data File(s)
Please Log In and visit the Product Manager to upload data files via the web form.

### Shell Script
Use the `re_upload` script to automate uploads from the *NIX command line. 

### Installation

To install the `re_upload` script directly from a Git repository, use `pip` with the `git+` command:

```sh
pip install git+https://github.com/nsteiner/re_upload.git
```  

### Usage

```sh
re_upload [-huojtcg1dxv] [-f [hours]] [-p [part]] [-k key|file] [-l "URI"] [-s server:port] file [name] [date] [time]

-h: Show help

-u: Check for update

Version: 62
-p: Designate file as part of a larger product (part # optional)

-f: Force overwrite if there is a conflict (hour range optional)

-o: Convert to COG (requires GDAL tools)

-j: Use JPEG compression (requires GDAL tools)

-t: Do not timeout

-k: Specify the upload key or file

-l: Specify a URI for download of the original data

-c: Add random sleep to mitigate concurrent uploads (e.g., cron jobs)

-g: Send through public gateway

-s: Specify the server and port

Default: https://realearth.ssec.wisc.edu
-1: Do not retry on failure

-d: Delete file on successful upload

-x: Print target server and port (do not upload)

-v: Be verbose

file: Path to file

Format: /path/to/[name]_[YYYYMMDD]_[HHMMSS].???
name: Specify the product name

Required when the file name does not contain [name]
Format: Cannot contain '_'
date: Specify the date

Required when the file name does not contain [date]
Format: YYYYMMDD
time: Specify the time

Required when the file name does not contain [time]
Format: HHMMSS
```