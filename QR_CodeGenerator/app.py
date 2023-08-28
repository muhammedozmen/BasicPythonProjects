# installing all the libraries needed
# creating a function that collects a text and converts it to a QR Code
# save the QR Code as an image
# run the function

import qrcode

def generate_qrcode(text, imgName):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save(imgName + ".png")

url = input("Enter your url: ")
img_name = input("Enter your image name: ")
generate_qrcode(url, img_name)