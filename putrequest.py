import requests
import pandas as pd
import json

api_url = "https://jsonplaceholder.typicode.com/todos/10"

# Beyond GET and POST, requests provides support for all the other HTTP methods you would use with a REST API. 
# The following code sends a PUT request to update an existing todo with new data. 
# Any data sent with a PUT request will completely replace the existing values of the todo.
# JSONPlaceholder endpoint you used with GET and POST, but this time you’ll append 10 to the end of the URL.
response=requests.get(api_url)
api_data=response.json()
print(api_data)

todo = {
    "userId": 1, 
    "title": "Wash car", 
    "completed": True
}

response = requests.put(api_url, json=todo)
print(response.json())

# The requested action was successful.
print(response.status_code) ## 200
