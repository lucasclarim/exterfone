import RPi.GPIO as GPIO
import time
from pushetta import Pushetta

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.IN, pull_up_down=GPIO.PUD_UP)
p = Pushetta("db0848c45ef6c59cdedd72c7fac5ccf6fc006357")
while True:
	input_state = GPIO.input(32)
	if input_state == False:
		p.pushMessage("campainha", "A campainha esta tocando.")
		print('Sending Notification')
		time.sleep(1)


