import requests
import pandas as pd
import json

api_url = "https://jsonplaceholder.typicode.com/todos/10"

#  if you want to completely remove a resource, then you use DELETE. Here’s the code to remove a todo:
response=requests.get(api_url)
api_data=response.json()
print(api_data)

response = requests.delete(api_url)
print(response.json())

# requests.delete() with an API URL that contains the ID for the todo you would like to remove. 
# This sends a DELETE request to the REST API, which then removes the matching resource.
# After deleting the resource, the API sends back an empty JSON object indicating that the resource has been deleted.
# The requests library is an awesome tool for working with REST APIs and an indispensable part of your Python tool belt.

#The requested action was successful.  200
print(response.status_code)