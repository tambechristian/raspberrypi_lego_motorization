import pygame
import RPi.GPIO as GPIO
import os
import time

#from picamera import PiCamera
from datetime import datetime

screen = pygame.display.set_mode([240, 160])

#camera = PiCamera()
#camera.resolution = (1280, 720)
#camera.framerate = (25)

in1= 4 #forward
in2 = 14 #backward
pwm_freq = 100 #pwm freq set at 2 KHz #duty cycle is in percentage
rec = 29

#record = 0

#set GPIO num
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
#GPIO.setup(rec, GPIO.OUT)

#setup PWM control
speedforward = GPIO.PWM(in1, pwm_freq)
speedbackward = GPIO.PWM(in2, pwm_freq)
speedforward.start(100)  #duty cycle is in percentage
speedbackward.start(100) #duty cycle is in percentage


try:
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
				elif event.key == pygame.K_s:
					os.system('sudo shutdown now')
				#elif event.key == pygame.K_r:
				#	if record == 0:
				#		record = 1
				#		moment = datetime.now()
				#		GPIO.output(rec, False)
				#		camera.start_recording('/home/pi/Vid_%02d')
				#elif event.key == pygame.K_t:
				#	if record == 1:
				#		record = 0
				#		GPIO.output(rec, True)
				#		camera.stop_recording()
				elif event.key == pygame.K_UP:
					GPIO.output(in1, True)
					GPIO.output(in2, False)
				elif event.key == pygame.K_DOWN:
					GPIO.output(in1, False)
					GPIO.output(in2, True)
				elif event.key == pygame.K_1:
					speedforward.ChangeDutyCycle(75) #duty cycle is in percentage
					speedbackward.ChangeDutyCycle(75) #duty cycle is in percentage
				elif event.key == pygame.K_2:
					speedforward.ChangeDutyCycle(85) #duty cycle is in percentage
					speedbackward.ChangeDutyCycle(85) #duty cycle is in percentage
				elif event.key == pygame.K_3:
					speedforward.ChangeDutyCycle(100) #duty cycle is in percentage
					speedforward.ChangeDutyCycle(100) #duty cycle is in percentage
			if event.type == pygame.KEYUP:
				GPIO.output(in1, False)
				GPIO.output(in2, False)

finally:
	GPIO.cleanup()

