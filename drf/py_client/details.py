import requests 

endpoint= "http://localhost:8080/api/products/1"

getResponse = requests.get(endpoint)
print(getResponse.json)