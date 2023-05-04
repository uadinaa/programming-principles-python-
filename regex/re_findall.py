import re 

text = (input())
x = re.findall("ab*",text)

abb=[]

for i in x:
  d = str(i).count('b')
  if d > 0 and d <= 3:
     abb.append(i)
  
if abb:
    print(abb)
else:
    print("no matches")