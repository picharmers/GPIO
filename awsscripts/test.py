#!/usr/bin/python

import os
from S3Operations import S3Operations as s3ops

s3 = s3ops()
#s3.listBuckets()
#s3.createBucket('traffic-logs')
#s3.putString('test\ttest\t', os.path.join('traffic-logs'))
s3.putFile('instrument-mapper.py', 'motown-emr')
