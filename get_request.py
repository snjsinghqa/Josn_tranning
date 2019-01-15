import json
import requests
import jsonpath

# data_req = '{"key1": "val1", "key2": "val2"}'
# res_data = json.loads(data_req)
# print res_data['key1']

# Make a request

api_url = 'https://reqres.in/api/uesr?page=2'
response1 = requests.get(api_url)
print (response1)
print (response1.text)

# Validate Status Code

assert response1.status_code == 200

# Parse  in to JSON Formate

json_response = json.loads(response1.text)
print json_response

# Apply JSON PATH
out_put1 =jsonpath.jsonpath(json_response,'data[0].year')
print out_put1[0]

for val in json_response['data']:
    print val['pantone_value']
