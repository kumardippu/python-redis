## Developed by Dippu
# Developed at 12-10-2022
# Purpose : Python - Redis library
import rds
import config
import csv

'''
## Some commands
# redis-cli
# hset pin_asp 804452 3ST # to set details of element here pin_asp is the name of hset and 804452 is the member , 3ST is the value
# hget pin_asp 804452 # to get details of element here pin_asp is the name of hset and 804452 is the member
# hdel pin_asp "804452" # delete hset 'pin_asp' is hset "804452" is element
# del pin_asp # delete all data
# FLUSHALL # delete everything from the redis
# hlen pin_asp # count data within hasmap


'''

class AspPinMapping():
	def __init__(self):
		self.file_name = config.PIN_FILE_NAME
		self.r = rds.getRedisObj()
	def readFile(self):
		file = open(self.file_name, 'r')
		reader = csv.reader(file, delimiter=',')
		for row in reader:
			pin_code = row[0]
			asp = row[3]
			##print(row[3])
			#self.setPinAsp(pin_code,asp)
			self.hSetPinAsp('pin_asp',pin_code,asp)

	def setPinAsp(self,pin,asp):
		print(pin,asp)
		self.r.set(pin, asp)
		
	def getDetailByPin(self,pin):
		asp = self.r.get(pin)
		return asp

	def getHashDetailByPin(self,hash_name,pin):
		asp = self.r.hget(hash_name,pin)
		return asp

	def hSetPinAsp(self,hash_name,pin,asp):
		#r.set(pin, asp)
		print(hash_name,pin,asp)
		self.r.hset(hash_name,pin, asp)

	def getAllDetail(self,key_name='pin_asp'):
		data = self.r.hgetall(key_name)
		return data


## Creating object
obj = AspPinMapping()
#data = obj.getAllDetail()
#data = obj.getDetailByPin('804452')
data = obj.getHashDetailByPin('pin_asp','804452')
#data = obj.readFile()
print(data)

