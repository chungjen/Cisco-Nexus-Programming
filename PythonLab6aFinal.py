
import ciscosparkapi
import requests
import datetime
import time
import os
import json

# User Input and global/static variables
SPARK_ACCESS_TOKEN = "PUT YOUR TEAMS TOKEN HERE"
SPARK_ROOM_ID = "Y2lzY29zcGFyazovL3VzL1JPT00vNzk4NTBmNTAtYjc1NC0xMWU5LWE1MjUtOTczYzJmNzQzYTZj"
switchuser='admin'
switchpassword='cisco@123'
url='http://10.36.197.71/ins'
myheaders={'content-type':'application/json'}

def interface_updown(status):

    if status == 'up':
        payload={
            "ins_api": {
            "version": "1.0",
            "type": "cli_conf",
	        "chunk": "0",
            "sid": "1",
            "input": "conf t ;int e1/1 ;no shut",
            "output_format": "json"
            }
        }
    else:
        payload={
            "ins_api": {
            "version": "1.0",
            "type": "cli_conf",
	        "chunk": "0",
            "sid": "1",
            "input": "conf t ;int e1/1 ;shut",
            "output_format": "json"
            }
        }

    try:
        response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

# Main
#
for i in range(4):
    if int(i%2) == 0:
        interface_updown("up")
        print("Interface up!")
    else:
        interface_updown("down")
        print("Interface down!")
    time.sleep(5)
