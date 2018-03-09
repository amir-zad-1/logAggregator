import sys
import requests as r

url = "http://localhost:8000/newlog"
#log_file = open("/var/log/nginx/logAggregator.access.log", "r")

for l in sys.stdin: #log_file:
    #r.post(url, data=l)
    print("[x]")
