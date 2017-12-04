from PIL import Image

icons = {
	"IconNotificationDefault-ldpi.png": 16,
	"IconNotificationDefault-ldpi-v9.png": 16,
	"IconNotificationDefault-ldpi-v11.png": 16,

	"IconNotificationDefault-mdpi.png": 24,
	"IconNotificationDefault-mdpi-v9.png": 24,
	"IconNotificationDefault-mdpi-v11.png": 24,

	"IconNotificationDefault-hdpi.png": 36,
	"IconNotificationDefault-hdpi-v9.png": 36,
	"IconNotificationDefault-hdpi-v11.png": 36,

	"IconNotificationDefault-xhdpi.png": 48,
	"IconNotificationDefault-xhdpi-v9.png": 48,
	"IconNotificationDefault-xhdpi-v11.png": 48,

	"IconNotificationDefault-xxhdpi.png": 72,
	"IconNotificationDefault-xxhdpi.png-v9.png": 72,
	"IconNotificationDefault-xxhdpi.png-v11.png": 72,

	"IconNotificationDefault-xxxhdpi.png": 96,
	"IconNotificationDefault-xxxhdpi.png-v9.png": 96,
	"IconNotificationDefault-xxxhdpi.png-v11.png": 96,

	"ic_onesignal_large_icon_default.png": 256,
}

for name in icons:
	im = Image.open( "upload.png" )
	im.thumbnail((icons[name], icons[name]), Image.ANTIALIAS)
	im.save(name, "PNG")
	im.close()