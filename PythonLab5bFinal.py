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
    "input": "show interface eth1/1-10",
    "output_format": "json"
  }
}

try:
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

#print(response)
#print(json.dumps(response,indent=4))

result = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']

#for i in range(len(result)):
#    print(result[i]['interface'])
#    print(result[i]['state'])
#    print(result[i]['admin_state'])

print('{0:15}   {1:10}   {2:10}'.format('interface','state','admin_state'))
print('{0:15}   {1:10}   {2:10}'.format('=========','=====','==========='))
for i in range(len(result)):
    print('{0:15}   {1:10}   {2:10}'.format(result[i]['interface'],result[i]['state'],result[i]['admin_state']))
