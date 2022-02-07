import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

in1 = 4 #forward
in2 = 14 #backward
dc = 50 #default duty cycle
temp = 1 

GPIO.setmode(GPIO.BCM) #braodcom soc channel: numbers after gpio
GPIO.setup(in1, GPIO.OUT) #set in1 as output
GPIO.setup(in2, GPIO.OUT) # set in2 as output
GPIO.output(in1, GPIO.LOW) # set in1 value to low
GPIO.output(in2, GPIO.LOW) # set in2 value to low
pwm1 = GPIO.PWM(in1, 1000) #set pwm signal and freq for in1
pwm2 = GPIO.PWM(in2, 1000) # set pwm signal and freq for in2


pwm1.start(dc) #start PWM
print("\n")
print("The default speed & direction of motor is Low & Forward")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")

while(1):

	x=input()
	if x == 'r':
		print("run")
		if (temp == 1):
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			print("forward")
			x='z'
		else:
			GPIO.output(in1, GPIO.LOW)
			GPIO.output(in2, GPIO.HIGH)
			print("backward")
			x='z'

	elif x=='s':
		print("stop")
		GPIO.output(in1, GPIO.LOW)
		GPIO.output(in2, GPIO.LOW)

	elif x=='f':
		print("forward")
		GPIO.output(in1, GPIO.HIGH)
		GPIO.output(in2, GPIO.LOW)
		temp=1
		x='z'

	elif x=='b':
		print("backward")
		GPIO.output(in1, GPIO.LOW)
		GPIO.output(in2, GPIO.HIGH)
		temp=0
		x='z'

	elif x=='l':
		print("low speed")
		pwm1.ChangeDutyCycle(25)
		x='z'

	elif x=='m':
		print("medium speed")
		pwm1.ChangeDutyCycle(65)
		x='z'

	elif x=='h':
		print("high speed")
		pwm1.ChangeDutyCycle(95)
		x='z'

	elif x=='e':
		GPIO.cleanup()
		print("GPIO clean up")
		break

	else:
		print("<<<   Wrong Data   >>>")
		print("please enter the defined data to continue...")


