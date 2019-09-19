import requests
import json

"""
Modify these please
"""
switchuser='admin'
switchpassword='cisco@123'

url='http://10.36.197.71/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "conf t ;int e1/1 ;no switchport ;ip address 192.168.11.1/24 ;no shut",
    "output_format": "json"
  }
}

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

#print(response)
print(json.dumps(response,indent=4))
