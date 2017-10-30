#!/usr/bin/env python

import time, sys, logging
from daemon2x import Daemon
from lib_oled96 import ssd1306
from PIL import ImageFont, ImageDraw, Image
from smbus import SMBus

# Logging
logging.basicConfig(filename='/home/oled/lib_oled96/clock.log',
                            filemode='a',
							format='[%(asctime)s] %(message)s',
							datefmt='%Y/%d/%m %H:%M:%S',
                            level=logging.INFO)

# Setup display
i2cbus = SMBus(1)		# 1 = Raspberry Pi but NOT early REV1 board
oled = ssd1306(i2cbus)	# create oled object, nominating the correct I2C bus, default address
draw = oled.canvas		# "draw" onto this canvas, then call display() to send the canvas contents to the hardware.

# Hello World
#oled.canvas.text((40,40),    'Hello World!', fill=1)

#Setup fonts
#font = ImageFont.load_default()
font1 = ImageFont.truetype('/home/pi/oled/DSEG/fonts/DSEG7-Modern/DSEG7Modern-Bold.ttf', 37)
font2 = ImageFont.truetype('/home/pi/oled/DSEG/fonts/DSEG7-Modern/DSEG7Modern-Bold.ttf', 12)

class MyDaemon(Daemon):
	def run(self):
		logging.info('--------------')
		logging.info('Daemon Started')
		
#		oled.cls()
		
		while True:
			draw.rectangle((0, 0, 128, 64), outline=0, fill=0)
#			oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)	# Border

			draw.text((0 ,  3), time.strftime("%I:%M"), font=font1, fill=1)
#			if time.strftime("%I")[:1] == '0':		#remove leading 0 for hour
#				draw.text((0, 3), '0', font=font1, fill=0)
#			draw.text((58,  0), time.strftime("%p")[:1], font=font3, fill=1)
			draw.text((15 , 48), time.strftime("%d-%m-%Y"), font=font2, fill=1)
			oled.display()
			
			time.sleep(-time.time() % 60)
			
		logging.info('Daemon Ended')


if __name__ == "__main__":
        daemonx = MyDaemon('/tmp/daemon-OLEDclock.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemonx.start()
                elif 'stop' == sys.argv[1]:
                        logging.info('Daemon Stopped')
                        daemonx.stop()
                elif 'restart' == sys.argv[1]:
                        logging.info('Daemon restarting')
                        daemonx.restart()
                else:
                        print("Unknown command")
                        sys.exit(2)
                sys.exit(0)
        else:
                print("usage: %s start|stop|restart" % sys.argv[0])
                sys.exit(2)
