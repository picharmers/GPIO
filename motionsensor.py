#!/usr/bin/python

import time

import RPi.GPIO as GPIO

pir_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

input_value = GPIO.input(pir_pin)

current_state = 0
previous_state = 0

print "Wait for PIR to be Ready"

while GPIO.input(pir_pin) == 1:
		current_state = 0

print "Ready"
'''
while True:
	if GPIO.input(pir_pin):
		print "Yes"

	time.sleep(0.1)
'''
while True:
	current_state = GPIO.input(pir_pin)
	if current_state==1 and previous_state==0:
		print "Motion Detected"
		previous_state = 1
	elif current_state==0 and previous_state==1:
		print "Ready"
		previous_state = 0
	
	time.sleep(0.01)

