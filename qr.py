import pyqrcode
url="http://www.github.com/sivaneshwaran019"
s=pyqrcode.create(url)
s.svg('Qr.svg',scale=10)
