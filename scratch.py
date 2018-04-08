import os,re

files = []
paths = []
line = ""
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "toplist-sorted.txt")) as file:
    lines = [line.strip() for line in file]
    print(lines)
for check in lines:
    # print(check)
    match = re.search(r"[a-zA-Z0-9-_.]+\..*", check)
    if match:
        files.append(match)
        print("Match!")
    else:
        paths.append(match)
        print("No Match!")
print("Files:")
print(files)
print("Paths:")
print(paths)
print("Lines:")
print(lines)
print("Local Scratch Complete")
# /