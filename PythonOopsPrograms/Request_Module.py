import requests

# GET REQUEST.
r = requests.get("https://www.google.com")
print(r.text)
print(r.status_code)

# POST REQUEST.
url = "www.something.com"
data = {
    "p1":4,
    "p2":8,
    "p3":16
}

# r1 = requests.post(url=url, data=data)

