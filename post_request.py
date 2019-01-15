import requests
import json
import jsonpath

url = 'https://reqres.in/api/users'
data_dict = {
    "name": "Sanjay Singh Panwar",
    "job": "leader"
}
response = requests.post(url,data_dict)
print (response.content)

assert response.status_code == 201

response_json = json.loads(response.text)
print response_json

name = jsonpath.jsonpath(response_json,'name')
print name[0]