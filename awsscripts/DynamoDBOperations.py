import boto.dynamodb
import time
import os

class DynamoDBOperations:
	
	db = None
	
	hash_key = None
	range_key = None

	def __init__(self):
		self.db = boto.dynamodb.connect_to_region('us-east-1')

	def listTables(self):
		return self.db.list_tables()
	
	def getKeyElements(self, table_name): 
		desc = self.db.describe_table(table_name)
		
		self.hash_key = desc['Table']['KeySchema']['HashKeyElement']['AttributeName']
		self.range_key = desc['Table']['KeySchema']['RangeKeyElement']['AttributeName']

	def insertData(self, data = dict(), table_name=None):

		table = self.db.get_table(table_name)
		item = table.new_item(hash_key=data['hash_key'], range_key = data['range_key'], attrs = data['attrs'])
		item.put()
