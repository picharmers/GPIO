#!/usr/bin/python

from DynamoDBOperations import DynamoDBOperations as ddb

table_name = 'MOTOWN_EVENT_LOG'
db = ddb()

db.getKeyElements(table_name)
#print db.getKeyElements(table_name)

data = {'hash_key': 'east_mall', 'range_key' : 'east_entrance','attrs' : {'timestamp': '2014042009'}}
print db.insertData(data, table_name)
