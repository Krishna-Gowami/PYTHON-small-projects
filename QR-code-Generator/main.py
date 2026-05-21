import qrcode
import os
from PIL import Image

qr = qrcode.QRCode()
QRpng_path = r"C:\Users\krish\OneDrive\Desktop\New folder\QR code generator\Output-png"
qr_counter_path = r"C:\Users\krish\OneDrive\Desktop\New folder\QR code generator\Output-png\QR_Code_counter\QRCounter.txt"
qr_counter = 1

url = input("Enter the URL to generate QR code: ")

qr.add_data(url)
img=qr.make_image()

try:
    with open (qr_counter_path,"a+") as file:
        last = file.tell()
        if last == 0:
            qr_counter = 1
            file.write(".")
        else:
            qr_counter = last +1
            file.write(".")
    file.close()
except Exception as e:
    print("An error occurred while updating the QR code counter:", e)

name = input("Enter the name of the QR code file: ")

img.save(f"{QRpng_path}\\QR-{name}-{qr_counter}.png") #QR-number- .... {name} that is taken in line 28
print("QR code generated and saved successfully.")


#open freshly created QR code


files = [
    os.path.join(QRpng_path, f)
    for f in os.listdir(QRpng_path)
    if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
]

latest_file = max(files, key=os.path.getmtime)

img = Image.open(latest_file)
img.show()

print("Opened:", os.path.basename(latest_file))