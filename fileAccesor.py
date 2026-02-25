import requests

ACCESS_TOKEN = "1iauuKUGD9BTXLDnsDpItZB3v03pbD0Y"
FOLDER_ID = "358896625450"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Get folder items
url = f"https://api.box.com/2.0/folders/{FOLDER_ID}/items"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    items = response.json()
    for item in items['entries']:
        print(item['name'])
else:
    print(f"Error: {response.status_code}")
    print(response.text)