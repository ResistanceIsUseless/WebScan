#/usr/bin/python
#Webscanner - Pykto
#TD: Make function for iterating through pages with parameters for all options
#TD: Decide on default scanning type (dirbuster or nikto)
#TD: Error handling(connection, missing pages,rtc),exporting data , hand off work to other scanners, api fuzzing,passive info gathering
import requests, argparse, urllib.parse

#argument parsing and helptext
parser = argparse.ArgumentParser()
parser.add_argument('-u', "--host", help="URL you wish to scan")
parser.add_argument('-p', "--path", help="Scan using specific path")
parser.add_argument('-r', "--robots", help="Check for robots.txt and check for disallow's", default='robots.txt', action ='store_true')
args = parser.parse_args()
if args.robots:
    print("Checking Robots")
    args.path = 'robots.txt'
    webhost = args.host
    path = args.path
    url = urllib.parse.urljoin(webhost, path)

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "00b85c94-437c-492d-bbaa-cfb0215421ad"
    }
    print(url)
    response = requests.request("GET", url, headers=headers)
    rpaths = []
    for lines in response.text.split("\n"):
        if "Disallow:" in lines:
            rpaths.append(lines.partition('Disallow: ')[2])

    print(rpaths)
#iterate through disallow lines checking status codes
    for path in rpaths:
        url = urllib.parse.urljoin(webhost, path)
        response = requests.request("GET", url, headers=headers)
        print(url)
        print(response.status_code)
        if response.status_code == '200':
            print("Success:" + url + response.status_code)


#if args.host:

