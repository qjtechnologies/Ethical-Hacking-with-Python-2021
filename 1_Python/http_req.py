import requests

response = requests.get(url="http://www.example.com")

print(response.status_code)
print(response.text)
