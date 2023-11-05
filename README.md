# QR Code Generator
This application is a simple command-line tool to generate QR codes from given URLs. The generated QR code is saved as an image file.

## Requirements
* Python 3.x


## Installation
```bash
pip install qrcode 
```

## Usage
```bash
python main.py --url <URL> [--filename <FILENAME>]
```
### Arguments
* --url or -u: The URL to be encoded in the QR code. This argument is required.
* --filename or -f: The filename for the generated QR code image. This argument is optional and defaults to "qr.png".

### Example
To generate a QR code for the URL "https://wiki.math.ntnu.no/tma4130/2023h/start" and save it as "wiki.png":
```bash
python main.py --url "https://wiki.math.ntnu.no/tma4130/2023h/start" --filename "wiki.png"
```
