import requests

url = "www.example.com"

r =request.get(url)

with open("file-name.html", "w") as f:
    f.write(r.text)