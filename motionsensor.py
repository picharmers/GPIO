#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from awsscripts.S3Operations import S3Operations as s3ops
from awsscripts.DynamoDBOperations import DynamoDBOperations as dbops
from datetime import datetime

s3 = s3ops()
db = dbops()
table_name = 'MOTOWN_EVENT_LOG'
pir_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

customer_id = 'east-mall'
device_id = 'east-entrance'
bucket_name = 'traffic-logs'

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
		print 'Motion detected'
		formattedtime = datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H')
		data = {'hash_key': '{customer_id}::{device_id}'.format(**locals()), 'range_key': str(time.time()), 'attrs':{}}
		db.insertData(data, table_name)
		previous_state = 1
	elif current_state==0 and previous_state==1:
		print "Ready"
		previous_state = 0
	
	time.sleep(0.01)

