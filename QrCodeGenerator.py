# data will work like an url.
#data will be converted into binary code and become a grid pack which black and white squares and error correction added 



# 1. take a data input
# 2. encode to QR format
# 3. Add error correction 
# 4. save as image

import qrcode

def create_qr(data, filename="my_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR saved as {filename}")

# ---- user input ----
data = input("Enter text or URL for QR code: ")
filename = input("Enter filename (example: myqr.png): ")

if filename.strip() == "":
    filename = "my_qr.png"

create_qr(data, filename)
