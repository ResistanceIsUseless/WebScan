# /usr/bin/python
# Webscanner - Pykto
# TD: Make function for iterating through pages with parameters for all options
# TD: Decide on default scanning type (dirbuster or nikto)
# TD: Error handling(connection, missing pages,rtc),exporting data ,
# hand off work to other scanners, api fuzzing,passive info gathering
# Async requests
import requests, argparse, urllib.parse, os, re

#argument parsing and helptext
parser = argparse.ArgumentParser()
parser.add_argument('-u', "--host", help="URL you wish to scan")
parser.add_argument('-p', "--path", help="Scan using specific path")
parser.add_argument('-r', "--robots", help="Check for robots.txt and check for disallow's", default='robots.txt', action ='store_true')
args = parser.parse_args()
rpaths = []
rpaths_good = []
found_files = []
imported_paths = []
imported_files = ['.bash_history', '.bashrc', '.DS_Store' ,'.DS_STORE', '.git/config', '.git/HEAD',
                  '.gitignore', '.history', '.htaccess', 'htpasswd', '.htpasswd', '.passwd', '.profile', '.psql_history',
                  '.rhosts','.settings', '.sh_history','.ssh/authorized_keys','.ssh/known_hosts', '.svn/entries']

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# sort paths and files
with open(os.path.join(__location__, "toplist-sorted.txt")) as file:
    file_db = [line.strip() for line in file]
for check in file_db:
    match = re.search(r"[a-zA-Z0-9-_.]+\..*", check)
    if match:
        imported_files.append(match)
    else:
        imported_paths.append(match)

# Check for robots.txt and store disallow paths if they are there
# if args.robots:
#     print("Checking Robots")
#     args.path = 'robots.txt'
#     webhost = args.host
#     path = args.path
#     url = urllib.parse.urljoin(webhost, path)
#
#     headers = {
#         'Cache-Control': "no-cache",
#
#     }
#     print(url)
#     response = requests.request("GET", url, headers=headers)
#     for lines in response.text.split("\n"):
#         if "Disallow:" in lines:
#             rpaths.append(lines.partition('Disallow: ')[2])
#
#     print(rpaths)
# # iterate through disallow lines checking status codes
#
#     for path in rpaths:
#         url = urllib.parse.urljoin(webhost, path)
#         response = requests.request("HEAD", url, headers=headers)
#         #print(url)
#         if response.status_code == requests.codes.ok:
#             print("Success:" + str(url) +" STATUS: " + str(response.status_code))
#


if args.host:
    # Grab Robots.txt
    print("Base Scan \nChecking for files")
    args.path = "robots.txt"
    webhost = args.host
    path = args.path
    url = urllib.parse.urljoin(webhost, path)
    headers = {
        'Cache-Control': "no-cache",
    }
    response = requests.request("GET", url, headers=headers)
    # Split robots.txt into paths and files
    for lines in response.text.split("\n"):
        if "allow:" in lines:
            rpaths.append(lines.partition('Disallow: ')[2])
    for check in rpaths:
        match = re.search(r"[a-zA-Z0-9-_.]+\..*", check)
        if match:
            imported_files.append(match)
        else:
            imported_paths.append(match)
    print("printing robots.txt")
    print(imported_paths + imported_files)


    for path in imported_files:
        url = urllib.parse.urljoin(webhost, path)
        headers = {
            'Cache-Control': "no-cache",
        }
        response = requests.request("HEAD", url, headers=headers)
        print(url)
        if response.status_code == requests.codes.ok:
            print("Success:" + str(url) + " STATUS: " + str(response.status_code))
            rpaths_good.append(path)


        # paths AND files from robots.txt are now saved to rpaths_good
        #
        # for lines in rpaths_good:
        #     path = rpaths_good + file_db
        #     url = urllib.parse.urljoin(webhost, path)
        #     response = requests.request("HEAD", url, headers=headers)
        #     print(url)
        #     if response.status_code == requests.codes.ok:
        #         print("Success:" + str(url) + " STATUS: " + str(response.status_code))
print(rpaths_good)
# Import file and try against found paths as well as root directory
# PULL FILE NAME FROM PATH ([a-zA-Z0-9-_.]+\..*)

