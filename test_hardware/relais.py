try:
	from RPi import GPIO
except ImportError:
	import _fake_GPIO as GPIO

import time

relay_pins = {1:2,2:3,3:4,4:27,5:22,6:5,7:6,8:13}
sleep_time = 0.1

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)   

for relay_pin, board_pin in relay_pins.items():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.HIGH)
	time.sleep(1)

time.sleep(1)

for relay_pin, board_pin in relay_pins.items():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.LOW)
	time.sleep(1)

time.sleep(1)

def float_pin(off, on):
	if (on != None):
		GPIO.output(on, GPIO.HIGH)
		time.sleep(sleep_time);
	if (off != None):
		GPIO.output(off, GPIO.LOW)
		time.sleep(sleep_time);

while True:
	for b in range(2):
		float_pin(None	             , relay_pins[1]  )
		float_pin(relay_pins[1]  , relay_pins[2]  )
		float_pin(relay_pins[2]  , relay_pins[3])
		float_pin(relay_pins[3], relay_pins[4] )
		float_pin(relay_pins[4] , relay_pins[5] )
		float_pin(relay_pins[5] , relay_pins[6]  )
		float_pin(relay_pins[6]  , relay_pins[7])
		float_pin(relay_pins[7], relay_pins[8])
		float_pin(relay_pins[8], relay_pins[1])
		float_pin(relay_pins[1], relay_pins[2]  )
		float_pin(relay_pins[2]  , relay_pins[3] )
		float_pin(relay_pins[3] , relay_pins[4] )
		float_pin(relay_pins[4] , relay_pins[5])
		float_pin(relay_pins[5], relay_pins[6]  )
		float_pin(relay_pins[6]  , relay_pins[7]  )
		float_pin(relay_pins[7]  , None               )
