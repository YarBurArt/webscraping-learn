import requests
import json

# set up the request parameters
params = {
  'api_key': 'demo',
  'q': 'pizza'
}

# make the http GET request to SerpWow
api_result = requests.get('https://api.serpwow.com/live/search', params)

# print the JSON response from SerpWow
print(json.dumps(api_result.json()))