#! /usr/bin/python
from PIL import Image

icons = {
	"android/Icon.png": 57,
	"android/Icon-ldpi.png": 36,
	"android/Icon-mdpi.png": 48,
	"android/Icon-hdpi.png": 72,
	"android/Icon-xhdpi.png": 96,
	"android/Icon-xxhdpi.png": 144,
	"android/Icon-xxxhdpi.png": 192,

	"ios/Icon-40.png": 40,
	"ios/Icon-58.png": 58,
	"ios/Icon-76.png": 76,
	"ios/Icon-80.png": 80,
	"ios/Icon-87.png": 87,
	"ios/Icon-120.png": 120,
	"ios/Icon-152.png": 152,
	"ios/Icon-167.png": 167,
	"ios/Icon-180.png": 180,
	"ios/Icon-1024.png": 1024,

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
	im.resize((icons[name], icons[name]), Image.ANTIALIAS)
	im.save(name, "PNG")
	im.close()
