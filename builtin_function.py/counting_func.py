import re

def counting(arr):
    for i in arr:
        x = re.findall("[a-z]", arr)
        y = re.findall("[A-Z]", arr)
        return len(x),len(y)
        
arr = input()
print(counting(arr))