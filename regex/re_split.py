import re

text = input()
x = re.split("(?=[A-Z])", text)  #?= это типа тик жакша, что б загл ариперди алу ушин
print(x)