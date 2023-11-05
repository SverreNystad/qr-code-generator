import qrcode
from PIL import Image

def generate_qr(url: str, filename="qr.png") -> Image:
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an Image object from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(filename)
    return img

# Example usage:
if __name__ == "__main__":
    url = "https://wiki.math.ntnu.no/tma4130/2023h/start"
    generate_qr(url, "wiki.png")

