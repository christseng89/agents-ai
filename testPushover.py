import requests
import os

res = requests.post("https://api.pushover.net/1/messages.json", data={
    "token": os.getenv("PUSHOVER_TOKEN"),
    "user": os.getenv("PUSHOVER_USER"),
    "message": "Test message from script"
})
print(res.status_code)
print(res.text)
