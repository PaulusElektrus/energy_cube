try:
	from RPi import GPIO
except ImportError:
	import _fake_GPIO as GPIO

import time


relay_pins = {1:14,2:15,3:18,4:23,5:24,6:25,7:8,8:7}
sleep_time = 1

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)   

for relay_pin, board_pin in relay_pins.items():
	GPIO.setup(board_pin, GPIO.OUT)


def float_pin(off, on):
	if (on != None):
		GPIO.output(on, GPIO.HIGH)
		time.sleep(sleep_time);
	if (off != None):
		GPIO.output(off, GPIO.LOW)
		time.sleep(sleep_time);


float_pin(14, None)
float_pin(None, 14)


