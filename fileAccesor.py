
from boxsdk import OAuth2, Client

# You'll need to set up OAuth credentials first
access_token = "U0krlwTj9JfFHq6JUAvvIOcD37D4PDZZ"
client = Client(OAuth2(access_token=access_token))

# Get the folder (use the ID from your URL: 358896625450)
folder = client.folder("358896625450")

# List items in the folder
for item in folder.get_items():
    print(item.name)