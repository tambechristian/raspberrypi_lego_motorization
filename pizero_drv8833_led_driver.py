import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

in1 = 21 #forward
in2 = 20 #backward
dc = 50 #default duty cycle #duty cycle is in percentage
en = 16
temp = 1 

GPIO.setmode(GPIO.BCM) #braodcom soc channel: numbers after gpio

GPIO.setup(in1, GPIO.OUT) #set in1 as output
GPIO.setup(in2, GPIO.OUT) # set in2 as output
GPIO.setup(en, GPIO.OUT) # set en as output

GPIO.output(en, GPIO.HIGH) # set en value to high to activate the chip
GPIO.output(in1, GPIO.LOW) # set ain1 value low to ov
GPIO.output(in2, GPIO.LOW) # set ain2 value low to ov

GPIO.output(in1, GPIO.HIGH) # set ain1 high to 3.3v. (volt across vm and aout1 (grnd) is 5v if vm=5v)
GPIO.output(in2, GPIO.HIGH) # set ain2 high to 3.3v. (volt across vm and aout2 (grnd) is 5v if vm= 5v)

#pwm1 = GPIO.PWM(in1, 2000) #set pwm signal and freq (1Khz) for in1
#pwm2 = GPIO.PWM(in2, 2000) # set pwm signal and freq (1Khz) for in2

#pwm1.start(dc) #start PWM

#pwm2.ChangeDutyCycle(95) #duty cycle is in percentage
#pwm1.stop()
#GPIO.output(in2, GPIO.HIGH)
