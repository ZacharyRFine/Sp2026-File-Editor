import requests

ACCESS_TOKEN = "U0krlwTj9JfFHq6JUAvvIOcD37D4PDZZ"
FOLDER_ID = "358896625450"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Get folder items
url = f"https://api.box.com/2.0/folders/{FOLDER_ID}/items"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    items = response.json()
    print(f"\nFiles in folder:")
    for i, item in enumerate(items['entries']):
        print(f"  {i}: {item['name']}")
    
    # Let user pick a file
    choice = input("\nEnter the number of the file to download: ")
    
    try:
        file_index = int(choice)
        selected_file = items['entries'][file_index]
        file_id = selected_file['id']
        file_name = selected_file['name']
        
        # Get file download URL
        print(f"\nGetting download link for {file_name}...")
        file_url = f"https://api.box.com/2.0/files/{file_id}"
        file_response = requests.get(file_url, headers=headers)
        
        if file_response.status_code == 200:
            file_info = file_response.json()
            download_url = file_info.get('download_url')
            
            if download_url:
                print(f"Download link: {download_url}")
                print(f"✓ You can download the file using this link")
            else:
                print("Could not get download URL")
        else:
            print(f"Error: {file_response.status_code}")
            
    except (ValueError, IndexError):
        print("✗ Invalid selection")
else:
    print(f"Error: {response.status_code}")
    print(response.text)