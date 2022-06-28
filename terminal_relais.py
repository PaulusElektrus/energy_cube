print("*** Hello to Terminal Relais Controler ***")
print("Press Strg + C to abort execution.")

try:
	from RPi import GPIO
except ImportError:
	import _fake_GPIO as GPIO

def switch(relay_pins, relais, status):
	try:
		board_pin = relay_pins[relais]
		if status == "on":
			GPIO.output(board_pin, GPIO.LOW)
			return
		if status == "off":
			GPIO.output(board_pin, GPIO.HIGH)
			return
		else:
			print("Status has to be on or off!")
			return 
	except KeyError:
		print("Relais number not in range 1-8!")

relay_pins = {1:14,2:15,3:18,4:23,5:24,6:25,7:8,8:7}

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)   

for relay_pin, board_pin in relay_pins.items():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.HIGH)

while True:

	relais = input("Enter relais number: ")
	status = input("Enter status (on/off): ")

	switch(relay_pins, int(relais), status)
