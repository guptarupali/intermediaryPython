import requests
url = "http://www.omdbapi.com/?t=the+social+network&apikey=72bc447a"

response = requests.get(url)
json_data = response.json()

print(json_data)

for keys, values in json_data.items():
    print(keys + " " + values)

