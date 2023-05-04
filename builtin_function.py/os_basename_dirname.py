import os

path = "/Users/altynai/pp1/2 sem/lab6/dina.txt"

if os.path.exists(path):
    print("file exists")

    print("filename :")
    print(os.path.basename(path))
    
    print("directory portion of the given path:")
    print(os.path.dirname(path))
else:
    print("no file like that")