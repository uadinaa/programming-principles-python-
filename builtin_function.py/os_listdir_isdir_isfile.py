import os

path = "/Users/altynai/pp1/2 sem/lab6"
dir_list = os.listdir(path)

print("\nonly directories:")
for i in dir_list:
    if os.path.isdir(os.path.join(path, i)):
        print(i)

print("\nonly files:")
for i in dir_list:
    if os.path.isfile(os.path.join(path, i)):
        print(i)

print("\nall directories and files", path ,":")
print(dir_list)