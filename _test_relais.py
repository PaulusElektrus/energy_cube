try:
	from RPi import GPIO
except ImportError:
	import _fake_GPIO as GPIO

import time

relay_pins = {'one': 11, 'two':7, 'three':12, 'four':16, 'five':18, 'six':22, 'seven':15, 'eight':13}
sleep_time = 0.1

GPIO.setmode(GPIO.BOARD)  
GPIO.setwarnings(True)   

for relay_pin, board_pin in relay_pins.items():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.HIGH)

for relay_pin, board_pin in relay_pins.items():
	GPIO.setup(board_pin, GPIO.OUT, GPIO.LOW)
	GPIO.output(board_pin, GPIO.LOW)

def float_pin(off, on):
	if (on != None):
		GPIO.output(on, GPIO.HIGH)
		time.sleep(sleep_time);
	if (off != None):
		GPIO.output(off, GPIO.LOW)
		time.sleep(sleep_time);

for b in range(2):
	float_pin(None	             , relay_pins['one']  )
	float_pin(relay_pins['one']  , relay_pins['two']  )
	float_pin(relay_pins['two']  , relay_pins['three'])
	float_pin(relay_pins['three'], relay_pins['four'] )
	float_pin(relay_pins['four'] , relay_pins['five'] )
	float_pin(relay_pins['five'] , relay_pins['six']  )
	float_pin(relay_pins['six']  , relay_pins['seven'])
	float_pin(relay_pins['seven'], relay_pins['eight'])
	float_pin(relay_pins['eight'], relay_pins['seven'])
	float_pin(relay_pins['seven'], relay_pins['six']  )
	float_pin(relay_pins['six']  , relay_pins['five'] )
	float_pin(relay_pins['five'] , relay_pins['four'] )
	float_pin(relay_pins['four'] , relay_pins['three'])
	float_pin(relay_pins['three'], relay_pins['two']  )
	float_pin(relay_pins['two']  , relay_pins['one']  )
	float_pin(relay_pins['one']  , None               )

