import requests

# URL for Stellarium's remote control (adjust port if different)
url = 'http://localhost:8090/api/main/time/set'
params = {
    'time': '2022-09-23T20:30:00',
    'action': 'set'
}

# Set Stellarium's time
response = requests.get(url, params=params)
print(response.text)

# Command to look at Mars
look_at_mars = 'http://localhost:8090/api/main/view/goto_object?target=Mars'
response = requests.get(look_at_mars)
print(response.text)
