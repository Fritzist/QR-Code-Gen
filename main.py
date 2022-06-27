import qrcode as qr
from qrcode.image.pil import PilImage

link = input("Enter the link to be encoded: ")
path = input("Enter the path where you want to save the QR-COde: ")
path = path + "/"
name = input("Enter the name of the QR-Code: ")

img = qr.make(link.__str__())

img.save(path + name + ".png")

img.show()

print(name.upper() + " was successfully generated! Check your path ( " + path + " ) for the QR-Code.")
