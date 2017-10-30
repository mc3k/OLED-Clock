#!/usr/bin/env python

from lib_oled96 import ssd1306
import time
#import sys
from PIL import ImageFont, ImageDraw#, Image

from smbus import SMBus
i2cbus = SMBus(1)        # 1 = Raspberry Pi but NOT early REV1 board

oled = ssd1306(i2cbus)   # create oled object, nominating the correct I2C bus, default address
draw = oled.canvas   # "draw" onto this canvas, then call display() to send the canvas contents to the hardware.

#Setup fonts
#font = ImageFont.load_default()
font1 = ImageFont.truetype('FreeSans.ttf', 40)
font2 = ImageFont.truetype('FreeSans.ttf', 17)
font3 = ImageFont.truetype('FreeSans.ttf', 12)


# put border around the screen:
#oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

while True:
	
	#print time.strftime("%I:%M:%S %p")
	
	draw.rectangle((0, 0, 128, 64), outline=0, fill=0)

	draw.text((0, 0), time.strftime("%I:%M"), font=font1, fill=1)
	if time.strftime("%I")[:1] == '0':		#remove leading 0 for hour
		draw.text((0, 0), '0', font=font1, fill=0)
	draw.text((105, 20), time.strftime("%S"), font=font2, fill=1)
	draw.text((106, 8), time.strftime("%p"), font=font3, fill=1)
	draw.text((40 , 45), time.strftime("%b %d, %Y"), font=font3, fill=1)
	
	oled.display()
	
	time.sleep(-time.time() % 1)
