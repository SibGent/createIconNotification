#! /usr/bin/python
from PIL import Image

icons = {
	"Icon.png": 57,
	"Icon-ldpi.png": 36,
	"Icon-mdpi.png": 48,
	"Icon-hdpi.png": 72,
	"Icon-xhdpi.png": 96,
	"Icon-xxhdpi.png": 144,
	"Icon-xxxhdpi.png": 192,

	"Icon-40.png": 40,
	"Icon-58.png": 58,
	"Icon-76.png": 76,
	"Icon-80.png": 80,
	"Icon-87.png": 87,
	"Icon-120.png": 120,
	"Icon-152.png": 152,
	"Icon-167.png": 167,
	"Icon-180.png": 180,
	"Icon-1024.png": 1024,

	"IconNotificationDefault-ldpi.png": 16,
	"IconNotificationDefault-mdpi.png": 24,
	"IconNotificationDefault-hdpi.png": 36,
	"IconNotificationDefault-xhdpi.png": 48,
	"IconNotificationDefault-xxhdpi.png": 72,
	"IconNotificationDefault-xxxhdpi.png": 96,
	# "ic_onesignal_large_icon_default.png": 256,
}

for name in icons:
	im = Image.open( "upload.png" )
	im.thumbnail((icons[name], icons[name]), Image.ANTIALIAS)
	im.save(name, "PNG")
	im.close()
