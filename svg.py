import requests

url = "https://framerusercontent.com/images/5ackAZCZrdZwBwTSpObexy0XN0.svg"
filename = "image.svg"

response = requests.get(url)

if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"SVG file downloaded successfully as '{filename}'")
else:
    print("Failed to download SVG file")
