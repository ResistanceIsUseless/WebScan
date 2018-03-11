#/usr/bin/python
#Webscanner
#TD: functions
#TD: Error handling for missing pages, passive info gathering, exporting data for other uses, hand off work to other scanners, api fuzzing
import requests
import argparse
import urllib.parse

#argument parsing and helptext
parser = argparse.ArgumentParser()
parser.add_argument('-u', "--host", help="URL you wish to scan")
parser.add_argument('-p', "--path", help="Scan using specific path")
parser.add_argument('-r', "--robots", help="Check for robots.txt and check for disallow's", default='robots.txt', action ='store_true')
args = parser.parse_args()
if args.robots:
    print("Checking Robots")
    args.path = 'robots.txt'
#if args.u:

whost = args.host
path = args.path
url = urllib.parse.urljoin(whost, path)

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