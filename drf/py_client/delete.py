# import requests 

# endpoint= "http://localhost:8080/api/products/10/delete/"

# getResponse = requests.delete(endpoint)
# print(getResponse.status_code)


import os 
import pathlib


fullPath = "Hashmap.zip"

ProjectUniqueName = pathlib.Path(fullPath).stem

print(ProjectUniqueName)