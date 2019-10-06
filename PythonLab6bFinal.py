
import ciscosparkapi
import requests
import datetime
import time
import os
import json

# User Input and global/static variables
SPARK_ACCESS_TOKEN = "PUT YOUR TEAMS TOKEN HERE"
SPARK_ACCESS_TOKEN = "MjE4NmFhNzAtNGFhZi00NWU4LWJmZDUtZGM5YjU4MGUyYTk5ZWFmYjMxZWQtNzA2_PF84_e2f0cc3e-4483-4688-b134-a0f359d78ccd"
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


def WebEx_Message_Sent(MsgText):

    # Create a Cisco Spark object
    spark = ciscosparkapi.CiscoSparkAPI(access_token=SPARK_ACCESS_TOKEN)

    # Sent Message to the group
    result = spark.messages.create(SPARK_ROOM_ID,text=MsgText)

    # Print the Message and return it
    #print(result)
    #print('\n\n')


# Main
#
for i in range(4):
    if int(i%2) == 0:
        interface_updown("up")
        WebEx_Message_Sent("Interface Up!")
        print("Interface up!")
    else:
        interface_updown("down")
        WebEx_Message_Sent("Interface Down!")
        print("Interface down!")
    time.sleep(5)
