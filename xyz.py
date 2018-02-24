from pyzbar.pyzbar import decode
from PIL import Image
[a]=decode(Image.open('/home/pi/Downloads/img1.jpg'))
print a[0]
