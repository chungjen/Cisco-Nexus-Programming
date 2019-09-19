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
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show version",
    "output_format": "json"
  }
}

try:
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
except requests.exceptions.RequestException as e:
    print e
    sys.exit(1)

#print(response)
print(json.dumps(response,indent=4))
