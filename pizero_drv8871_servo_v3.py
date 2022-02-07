import os
os.system('sudo pigpiod')
from gpiozero import Servo
import time
import numpy as np
#import pigpio
import pygame

from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory()
screen = pygame.display.set_mode([240, 160])

hw_pwm = 12
#pi = pigpio.pi()
#pi.set_mode(hw_pwm, pigpio.OUTPUT)
servo = Servo(hw_pwm, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

steps = 0

try:
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
				elif event.key == pygame.K_l:
					for steps in np.arange (steps, -1, -0.05):
						#pi.set_servo_pulsewidth(hw_pwm, steps)
						servo.value = steps;
				elif event.key == pygame.K_r:
					for steps in np.arange (steps, 1, 0.05):
						#pi.set_servo_pulsewidth(hw_pwm, steps)
						servo.value = steps;
			elif event.type == pygame.KEYUP:
				#pi.set_servo_pulsewidth(hw_pwm, 0)
				servo.value = None;

finally:
	servo.close()


