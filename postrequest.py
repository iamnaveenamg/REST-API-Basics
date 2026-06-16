import requests
import pandas as pd
import json

api_url = "https://jsonplaceholder.typicode.com/todos/"

# use requests to POST data to a REST API to create a new resource. 
# You’ll use JSONPlaceholder again, but this time you’ll include JSON data in the request.

#  Here’s the data that you’ll send:
todo = {
    "userId": 1,
    "title": "Buy milk",
    "completed": False
}

# This JSON contains information for a new todo item. Back in the Python REPL, run the following code to create the new todo:
# POST request to create resource
response = requests.post(api_url, json=todo)

# 1. Get the actual data out of the response object
api_data=response.json()
print("--- Raw Python Dict ---")
print(api_data)

# 2. Convert the dictionary data to a formatted string
json_string = json.dumps(api_data, indent=4)
print("\n--- Formatted JSON String ---")
print(json_string)

# 3. Flatten the dictionary data into a pandas table
df = pd.json_normalize(api_data)
print("\n--- Pandas DataFrame Table ---")
print(df)

# 4. POST multiple JSON Strings
todo1 = [
    {
        "userId": 1,
        "title": "New Product",
        "completed": False
    },
    {
        "userId":1,
        "title":"Milk",
        "completed": True
    }
]
response1 = requests.post(api_url, json=todo1)
print("It will print ths Multiple JSON POST Method")
print(response1.json())


#A new resource was created.
print(response.status_code) ## 201
