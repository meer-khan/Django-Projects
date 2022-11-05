import requests 

endpoint= "http://localhost:8080/api/products/6/update/"

data = {
    "title":"this field is completely new",
    "price" :1000.00
} 
getResponse = requests.put(endpoint,json=data)
print(getResponse.json())