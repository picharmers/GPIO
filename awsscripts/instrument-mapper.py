#!/usr/bin/python

import sys
import time
from datetime import datetime

for line in sys.stdin:
	line = line.strip()
	customer_id, device_id, timestamp = line.split('\t')
	
	formatted_time = datetime.fromtimestamp(float(timestamp)).strftime('%Y%m%d%H')
	print '\t'.join([customer_id, device_id, formatted_time, '1'])


