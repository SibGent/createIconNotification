from PIL import Image

icon_name = []
icon_name.append( "IconNotificationDefault-hdpi.png" )
icon_name.append( "IconNotificationDefault-hdpi-v4.png" )
icon_name.append( "IconNotificationDefault-hdpi-v9.png" )
icon_name.append( "IconNotificationDefault-hdpi-v11.png" )
icon_name.append( "IconNotificationDefault-ldpi.png" ) 
icon_name.append( "IconNotificationDefault-ldpi-v9.png" )
icon_name.append( "IconNotificationDefault-ldpi-v11.png" )
icon_name.append( "IconNotificationDefault-mdpi.png" )
icon_name.append( "IconNotificationDefault-mdpi-v9.png" )
icon_name.append( "IconNotificationDefault-mdpi-v11.png" )
icon_name.append( "IconNotificationDefault-xhdpi.png" )
icon_name.append( "IconNotificationDefault-xhdpi-v9.png" )
icon_name.append( "IconNotificationDefault-xhdpi-v11.png" )

icon_size = []
icon_size.append( 52 )
icon_size.append( 72 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )
icon_size.append( 52 )

for i in range(13):
	im = Image.open( "upload.png" )
	im.thumbnail((icon_size[i], icon_size[i]), Image.ANTIALIAS)
	im.save(icon_name[i], "PNG")
	im.close()