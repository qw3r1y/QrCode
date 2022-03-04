import qrcode

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=5)

giden_deger =  "OLUŞTURMAK İSTEDİGİNİZ YAZIYI BURAYA GİRİNİZ"


qr.add_data(giden_deger)

qr.make(fit=True)


pic = qr.make_image(fill_color="black",back_color="white")

pic.save("ik_qr_code.png")