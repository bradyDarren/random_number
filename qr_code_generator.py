import qrcode
import qrcode.image.svg  #this line was only used for the last implementetion.

# svg is used when you want to have a dynamic size
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("This is a super QR code", image_factory=factory)
svg_img.save("myqr.svg")


# below is another way to make a QR code with specific parameters
# qr = qrcode.QRCode(version=1,
#                   error_correction=qrcode.constants.ERROR_CORRECT_L,
#                   box_size=20,
#                   border=2)

# qr.add_data("https://www.google.com")
# qr.make(fit=True)

# qr code is not changing color check in the pip notes
# img = qr.make_image(fill_color="red", back_color="blue")
# img.save("practice.png")

# below is how we would simply create a single QR code

# img = qrcode.make("Hello, my name is Darren Brady")
# img.save("mycode.png")
