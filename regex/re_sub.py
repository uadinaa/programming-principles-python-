import re

text = input()
x = ("[ ,.]")
z = re.sub(x, ":", text)

print(z)