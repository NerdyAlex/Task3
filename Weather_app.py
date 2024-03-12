import requests
import json

# Make a GET request to an example API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response into a Python dictionary
    data = json.loads(response.text)
    print(data)
else:
    print('Error:', response.status_code)

