import redis
import config

def getRedisObj():
    r = redis.Redis(host=config.HOST,port=config.PORT, password=config.PASSWORD)
    return r

'''r.set('foo', 'bar')
value = r.get('foo')
print(value)'''