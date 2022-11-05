import requests 

endpoint= "http://localhost:8080/api/products/10/delete/"

data = {
    "title":"this field is completely new",
    "price" :32.99
} 
getResponse = requests.delete(endpoint)
print(getResponse.status_code)