## Developed by Dippu
# Developed at 12-10-2022
# Purpose : To generate redis object for Python
import redis
import config

def getRedisObj():
    r = redis.Redis(host=config.HOST,port=config.PORT, password=config.PASSWORD)
    return r