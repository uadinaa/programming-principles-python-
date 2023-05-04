import os

path = "/Users/altynai/pp1/2 sem/lab6/dina.txt"

if os.path.exists(path):
    print("exists :)")
    
    if os.access(path, os.R_OK):
        print("the path is readable")
    else:
        print("path is not readable :(")
    

    if os.access(path, os.W_OK):
        print("the path is writable")
    else:
        print("path is not writable :(")
    

    if os.access(path, os.X_OK):
        print("the path is executable")
    else:
        print("path is not executable :(")
else:
    print("path does not exist :(")