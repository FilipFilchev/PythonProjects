import qrcode

image = qrcode.make("Hello World!")
image.save("new_qr.png")




#More advanced

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=1)

qr.add_data("https://www.website.com")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("qr_advanced.png")