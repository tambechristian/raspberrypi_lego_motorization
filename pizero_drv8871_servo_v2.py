import os
os.system('sudo pigpiod')
from gpiozero import Servo
import time

import pigpio
import pygame

screen = pygame.display.set_mode([240, 160])

hw_pwm = 12
pi = pigpio.pi()
pi.set_mode(hw_pwm, pigpio.OUTPUT)

steps = 1500

try:
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
				elif event.key == pygame.K_l:
					for steps in range (steps, 500, -10):
						pi.set_servo_pulsewidth(hw_pwm, steps)
						#time.sleep(0.01)
				elif event.key == pygame.K_r:
					for steps in range (steps, 2500, 10):
						pi.set_servo_pulsewidth(hw_pwm, steps)
						#time.sleep(0.01)
			elif event.type == pygame.KEYUP:
				pi.set_servo_pulsewidth(hw_pwm, 0)

finally:
	pi.stop()


