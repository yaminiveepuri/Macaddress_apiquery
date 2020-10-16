import requests
import json
import re
import os

api_key= os.environ['api_key']
mac_address = os.environ['mac_address']
def validate_mac_address(mac_address):
    pattern = '^(([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})|([0-9a-fA-F]{2}[-]){5}([0-9a-fA-F]{2})|[0-9a-fA-F]{12})$'
    return not re.match(pattern, mac_address) is None
b= validate_mac_address(mac_address)
if b== False :
    print ("Enter a valid MAC address")
    exit
else :
    
    url = 'https://api.macaddress.io/v1?apiKey=%s&output=json&search=%s' %(api_key,mac_address)

    payload = {}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhOGJjMDg2OC0yYWFjLTQ3MmYtYmM5YS1kMWFkYTU3MzcwYzciLCJuYW0iOiJhZG1pbiIsImlzcyI6IlltRndZekUxWXpBeU1ERTRibTkyTWpodWN6QjNNSEptYkRCMyIsInJvbCI6ImFkbWluLHdvcmtmbG93LWFkbWluIiwiZXhwIjoxNTk4OTgyMDY5MDAwLCJmbm0iOiJhZG1pbiIsImxubSI6ImFkbWluIiwiZW1sIjoiYWRtaW5AYml6YXBwcy5jaXNjby5jb20iLCJzaWQiOiIyMGYwY2VkMC1lYzc2LTExZWEtYWU5OC04NTYwYWEwZmU2ZmUiLCJhZG0iOnRydWUsImlhdCI6MTU5ODk4MDI2OX0.dZsyT9CbUrgaOBWOikezCnY6eGE-Svcti-Giizum6NY'
    }


    response = requests.request("GET", url, headers=headers, data = payload)
    res=json.loads(response.text)
    final = [res]
    result= final[0]['vendorDetails'] ['companyName']
    print(result)