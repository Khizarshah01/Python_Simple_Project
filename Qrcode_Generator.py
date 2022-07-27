import qrcode as qr
img = qr.make("https://github.com/KaimonGate")
img.save("GitHub_Profile.jpg")