
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
    print(result)
    print('\n\n')



#def Mail_Sent(srv_ip,from,to_user,Message)

#    connect to Mail Server
#    Write the message to the user


# Main

for i in range(4):
    if int(i%2) == 0:
        interface_updown("up")
        #WebEx_Message_Sent(Key,"Interface up!")
        #Mail_Sent("10,36.197.44","admin@hello.com","user@hello.com","Interface up!")
        print("Interface up!")
    else:
        interface_updown("down")
        #WebEx_Message_Sent("Message down!")
        #Mail_Sent("10,36.197.44","admin@hello.com","user@hello.com","Interface down!")
        print("Interface down!")
    time.sleep(5)
