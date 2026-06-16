import requests
import pandas as pd
import json

api_url = "https://jsonplaceholder.typicode.com/todos/2"

# GET is one of the most common HTTP methods you’ll use when working with REST APIs. This method allows you to retrieve resources from a given API. 
# GET is a read-only operation, so you shouldn’t use it to modify an existing resource.

# GET request to retrieve resources
response = requests.get(api_url)

# 1. Get the actual data out of the response object
api_data = response.json()
print("--- Raw Python Dict ---")
print(api_data)

# 2. Convert the dictionary data to a formatted string (Fixed Line 16)
json_string = json.dumps(api_data, indent=4)
print("\n--- Formatted JSON String ---")
print(json_string)

# 3. Flatten the dictionary data into a pandas table
df = pd.json_normalize(api_data)
print("\n--- Pandas DataFrame Table ---")
print(df)

# 4. Get a list of Customers
api_url1 = "https://jsonplaceholder.typicode.com/todos/"

response1=requests.get(api_url1)
api_data1=response1.json()
df1=pd.json_normalize(api_data1)
print("\n--- Pandas DataFrame Table for List ---")
print(df1)


#The response data is formatted as JSON, a key-value store similar to a Python dictionary. 
# It’s a very popular data format and the de facto interchange format for most REST APIs.

# The requested action was successful.
print(response.status_code) # 200

print(response.headers["Content-Type"])
# 'application/json; charset=utf-8'