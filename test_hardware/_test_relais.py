try:
	from RPi import GPIO
except ImportError:
	import _fake_GPIO as GPIO

import time

relay_pins = {1:14,2:15,3:18,4:23,5:24,6:25,7:8,8:7}
sleep_time = 0.1

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)   

for relay_pin, board_pin in relay_pins.items():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.HIGH)

for relay_pin, board_pin in relay_pins.items():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.LOW)

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

