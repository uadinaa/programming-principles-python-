import os

path = "/Users/altynai/pp1/2 sem/lab6/text.txt"

if os.path.exists(path):
    os.remove("text.txt")
    print("file removed")
else:
    print("no file like that")