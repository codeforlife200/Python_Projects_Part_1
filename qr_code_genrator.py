# import package
# to install run - pip install qrcode
import qrcode

# setting the size and version for qrcode
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=4
)

# enter any data that you want to enter in data varible in string 
data = "https://www.youtube.com/channel/UCB6SfKNLTX2AS0c-YjaBVlg"

# adding data to qrcode
qr.add_data(data)
# just to be sure  
# fil=true to avoid data overflow error that comes when we don't specify the size  
qr.make(fit=True)

# making the qrcode and saving it
img = qr.make_image(fill="black", back_color="white")
img.save('qr.png')
