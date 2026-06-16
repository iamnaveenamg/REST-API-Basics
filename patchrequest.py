import requests
import pandas as pd
import json

api_url = "https://jsonplaceholder.typicode.com/todos/10"

# requests.patch() to modify the value of a specific field on an existing todo. 
# PATCH differs from PUT in that it doesn’t completely replace the existing resource. 
# It only modifies the values set in the JSON sent with the request.
response=requests.get(api_url)
api_data=response.json()
print(api_data)

todo = {"title": "Mow lawn"}

response = requests.patch(api_url, json=todo)
print(response.json())

#The requested action was successful.  200
print(response.status_code)