#!/usr/bin/env python

from lib_oled96 import ssd1306
import time, datetime
from PIL import ImageFont, ImageDraw

from smbus import SMBus
i2cbus = SMBus(1)        # 1 = Raspberry Pi, early REV1 boards use 0

oled = ssd1306(i2cbus)   # create oled object, nominating the correct I2C bus, default address
draw = oled.canvas   # "draw" onto this canvas, then call display() to send the canvas contents to the hardware.

#Setup fonts
font = ImageFont.load_default()

# put border around the screen:
#oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

while True:
	
	#print time.strftime("%I:%M:%S %p")

	draw.rectangle((0, 0, 128, 64), outline=0, fill=0)

	draw.text((0, 0), time.strftime("%I:%M:%S %p"), font=font, fill=1)
	draw.text((0 , 10), time.strftime("%a, %d %b %Y"), font=font, fill=1)
	
	oled.display()
	
	time.sleep(-time.time() % 1)
