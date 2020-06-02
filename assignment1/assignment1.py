from __future__ import unicode_literals

import redis


# fill in the following.
HOST = "redis-13426.c228.us-central1-1.gce.cloud.redislabs.com"
PWD = "hqjhFKcfFKEf3NEGlBT6Lp7tDRVr4NZi"
PORT = "13426"

redis1 = redis.Redis(host = HOST, password = PWD, port = PORT)

while True:
    msg = input("Please enter your query (type 'quit' or 'exit' to end):").strip()
    if msg == 'quit' or msg == 'exit':
        break
    if msg == '':
        continue
    print("You have entered " + msg + " for", end=' ')

   
    # Add your code here
    redis1.incr(msg)
    print(redis1.get(msg).decode('UTF-8'), end='')
    print(' times')
