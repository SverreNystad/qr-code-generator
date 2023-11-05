import argparse
from qr_generator import generate_qr

# Create argument parser
parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")

# Add arguments
parser.add_argument("-u", "--url", required=True, help="URL to be encoded in the QR code")
parser.add_argument("-f", "--filename", default="qr.png", help="Filename for the generated QR code image")

# Parse arguments
args = parser.parse_args()

# Generate QR code

generate_qr(args.url, args.filename)
