import requests
import json


#get request
u = "https://reqres.in/api/users/2"
response = requests.get(u)
assert response.status_code == 200
json_response = json.dumps(response.json(),indent=2)
print("json response body: ",json_response)


#post request
# u1 = "https://reqres.in/api/users"
# data = {
#     "name":"john",
#     "job":"engineer"
# }
# response = requests.post(u1,json=data)
# assert response.status_code == 201 #create
# json_response = json.dumps(response.json(),indent=2)
# print("json response body: ",json_response)


#put request
# u2 = "https://reqres.in/api/users/2"
# data = {
#     "name": "morpheus",
#     "job": "zion resident"
# }
# response = requests.put(u2,json=data)
# assert response.status_code == 200
# json_response = json.dumps(response.json(),indent=2)
# print("json response body: ",json_response)


#delete request
# u3 = "https://reqres.in/api/users/2"
# response = requests.delete(u3)
# assert response.status_code == 204
# print("data deleted successfully with status code: ",response.status_code)




