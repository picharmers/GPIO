import boto
import time
import os

class S3Operations:
	
	s3 = None
	
	def __init__(self):
		self.s3 = boto.connect_s3()
	
	def createBucket(self, bucket_name):
		bucket = self.s3.create_bucket(bucket_name)
	
	def listBuckets(self):
		return self.s3.get_all_buckets()

	def putString(self, data, bucket):
		filename = 'device1_{timestamp}.log'.format(timestamp = int(time.time()))
		print os.path.join(bucket, 'east-mall', filename)
		b = self.s3.get_bucket(bucket)
		k = b.new_key(os.path.join('east-mall', filename))
		k.set_contents_from_string(data)

	def putFile(self, filename, bucket):
		b = self.s3.get_bucket(bucket)
		k = b.new_key(os.path.join('libs', filename))
		k.set_contents_from_file(filename)
