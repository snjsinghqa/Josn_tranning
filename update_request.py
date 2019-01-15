import requests
import json
import jsonpath

url = 'https://reqres.in/api/users/2'
data_dict = {
    "name": "Sanjay Singh Panwar",
    "job": "leader"
}
response = requests.put(url,data_dict)
print(response)

assert response.status_code == 200

json_response = json.loads(response.text)
print json_response

updated_time = jsonpath.jsonpath(json_response, 'updatedAt')
print updated_time[0]