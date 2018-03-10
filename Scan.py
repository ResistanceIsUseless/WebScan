#/usr/bin/python
#Webscanner
#TD: functions
#TD: Error handling for missing pages, passive info gathering, exporting data for other uses, hand off work to other scanners, api fuzzing
import requests
import argparse
import urllib.parse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="URL you wish to scan")
parser.add_argument("path", help="Scan using specific path")
parser.add_argument("robots", help="Check for robots.txt and check for disallow's")
args = parser.parse_args()
if args.robots:
#    print("Checking Robots")
#if args.u:

host = "http://www.epa.gov"
path = "/robots.txt"
url = urllib.parse.urljoin(host, path)

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "00b85c94-437c-492d-bbaa-cfb0215421ad"
    }
print(url)
response = requests.request("GET", url, headers=headers)
r = response.text
rpaths = []
for lines in response.text.split("\n"):
    if "Disallow:" in lines:
        rpaths.append(lines.partition('Disallow: ')[2])


    #else:
        #print("ignore")

print(rpaths)