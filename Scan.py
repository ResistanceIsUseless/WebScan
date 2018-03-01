#/usr/bin/python
#Webscanner
import requests

url = "http://10.11.1.50/robots.txt"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "00b85c94-437c-492d-bbaa-cfb0215421ad"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
