import requests
import json

# URL of the web-hosted JSON file
url = "https://gitlab.com/voltagestudios/pyrepo/-/raw/main/pkgs.json?ref_type=heads"

# Send a GET request to the URL
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON content
    data = json.loads(response.text)
    try:
        json.dump(data, f)
    except Exception as e:
        print(e)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")