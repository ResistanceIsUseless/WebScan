#/usr/bin/python
#Webscanner - Pykto
#TD: Make function for iterating through pages with parameters for all options
#TD: Decide on default scanning type (dirbuster or nikto)
#TD: Error handling(connection, missing pages,rtc),exporting data , hand off work to other scanners, api fuzzing,passive info gathering
import requests, argparse, urllib.parse,

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
        response = requests.request("HEAD", url, headers=headers)
        #print(url)
        #print(response.status_code)
        if response.status_code == requests.codes.ok:
            print("Success:" + str(url) +" STATUS: "+ str(response.status_code))

if args.host
#scan through top domain checking for vulnerable files
    print("Base Scan \\n Checking for files")

    args.path = 'robots.txt'
    webhost = args.host
    path = args.path
    url = urllib.parse.urljoin(webhost, path)

    headers = {
        'Cache-Control': "no-cache",
         'Postman-Token': "00b85c94-437c-492d-bbaa-cfb0215421ad"
    }
    response = requests.request("GET", url, headers=headers)
    for lines in response.text.split("\n"):
        if "allow:" in lines:
            rpaths.append(lines.partition('allow: ')[2])

    print(rpaths)
rpaths_good = []
found_files = []
# iterate through robots checking status codes
# prob should create new object to store valid paths after printing them
    for path in rpaths:
        url = urllib.parse.urljoin(webhost, path)
        response = requests.request("HEAD", url, headers=headers)
        # print(url)
        # print(response.status_code)
        if response.status_code == requests.codes.ok:
            print("Success:" + str(url) + " STATUS: " + str(response.status_code))
            rpaths_good.append(path)
 #import file and try against found paths as well as root directory
    open(files.txt, str, fpath)
    for path in rpaths_good
        url = urllib.parse.urljoin(webhost, path)
        response = requests.request("HEAD", url, headers=headers)
        # print(url)
        # print(response.status_code)
        if response.status_code == requests.codes.ok:
        print("Success:" + str(url) + " STATUS: " + str(response.status_code))
        found_files.append(path)


