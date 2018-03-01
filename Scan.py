#/usr/bin/python
#Webscanner
import requests

url = "http://www.epa.gov/robots.txt"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "00b85c94-437c-492d-bbaa-cfb0215421ad"
    }

response = requests.request("GET", url, headers=headers)
r = response.text

for line in response.text.split("\n"):
#This is doing the opposite, looking online i probably need another for loop
    if line.find("Disallow:"):
        print(line)