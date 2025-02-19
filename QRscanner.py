import qrcode # type: ignore

# Data to be encoded
data = "papugd1332005@gmail.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="purple", back_color="white")  # Corrected fill_color

# Save the image
img.save("qrcode.png")
