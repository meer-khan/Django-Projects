import requests

# endpoints = 'https://httpbin.org/anything'
endpoints = 'http://localhost:8081/'

getResponse = requests.get(endpoints , json={'Data' : 'Hello'})
print (getResponse.json())
getResponse = requests.get(endpoints , data= {'Data' : 'Hello2'})
print ('\n',getResponse.json())
getResponse = requests.get(endpoints)
print ('\n',getResponse.json())

# getting status code of the URL response 

getResponse = requests.get(endpoints)
print("*"*50)
print(getResponse.status_code)