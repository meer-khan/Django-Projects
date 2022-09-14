import requests

# endpoints = 'https://httpbin.org/anything'
endpoints = 'http://localhost:8080/api/'

getResponse = requests.get(endpoints ,params={'params':'Query Parameters'}, json={'Data' : 'Hello'})
print (getResponse.json())


# getResponse = requests.get(endpoints , data= {'Data' : 'Hello2'})
# print ('\n',getResponse.json())
# getResponse = requests.get(endpoints)
# print ('\n',getResponse.json()['data'])

# # getting status code of the URL response 

# getResponse = requests.get(endpoints)
# print("*"*50)
# print(getResponse.status_code)




# import re
# value=['[a,b,c]', '[d,e,f]']
# output = []
# for i in value:
#     charactersList = []
#     val = re.sub(",","",i[1:-1])
#     for j in val:
#         charactersList.append(j)
#     output.append(charactersList)
# print(output)



