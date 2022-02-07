import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

in1 = 4 #forward
in2 = 14 #backward
dc = 50 #default duty cycle #duty cycle is in percentage
temp = 1 

GPIO.setmode(GPIO.BCM) #braodcom soc channel: numbers after gpio
GPIO.setup(in1, GPIO.OUT) #set in1 as output
GPIO.setup(in2, GPIO.OUT) # set in2 as output
GPIO.output(in1, GPIO.LOW) # set in1 value to low
GPIO.output(in2, GPIO.LOW) # set in2 value to low
pwm1 = GPIO.PWM(in1, 1000) #set pwm signal and freq (1Khz) for in1
pwm2 = GPIO.PWM(in2, 1000) # set pwm signal and freq (1Khz) for in2

direction  = 'forward'
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
			direction = 'forward'
			#x='z'
		else:
			GPIO.output(in1, GPIO.LOW)
			GPIO.output(in2, GPIO.HIGH)
			direction = 'backward'
			print("backward")
			#x='z'

	elif x=='s':
		print("stop")
		GPIO.output(in1, GPIO.LOW)
		GPIO.output(in2, GPIO.LOW)

	elif x=='f':
		print("forward")
		direction = 'forward'
		GPIO.output(in1, GPIO.HIGH)
		GPIO.output(in2, GPIO.LOW)
		temp=1
		#x='z'

	elif x=='b':
		print("backward")
		direction = 'backward'
		GPIO.output(in1, GPIO.LOW)
		GPIO.output(in2, GPIO.HIGH)
		temp=0
		#x='z'

	elif x=='l':
		if direction == 'forward':
			print("low speed forward")
			pwm1.ChangeDutyCycle(25)  #duty cycle is in percentage
			#x='z'
		else:
			pwm1.stop()
			print("low speed backward")
			pwm2.start(25)  #duty cycle is in percentage
			pwm2.ChangeDutyCycle(25)  #duty cycle is in percentage

	elif x=='m':
		if direction == 'forward':
			print("medium speed")
			pwm1.ChangeDutyCycle(65)  #duty cycle is in percentage
			#x='z'
		else:
			pwm1.stop()
			print("medium speed backward")
			pwm2.start(65)  #duty cycle is in percentage
			pwm2.ChangeDutyCycle(65) #duty cycle is in percentage
	elif x=='h':
		if direction == 'forward':
			print("high speed")
			pwm1.ChangeDutyCycle(95) #duty cycle is in percentage
			#x='z'
		else:
			pwm1.stop()
			print("high speed backward")
			pwm2.ChangeDutyCycle(95) #duty cycle is in percentage
			#x='z'

	elif x=='e':
		GPIO.cleanup()
		print("GPIO clean up")
		break

	else:
		print("<<<   Wrong Data   >>>")
		print("please enter the defined data to continue...")


