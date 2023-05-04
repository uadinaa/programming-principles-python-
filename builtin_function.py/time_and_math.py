import time
import math
y = int(input())
x = int(input())
z = x / 1000
time.sleep(z)
result = math.sqrt(y)

print("Square root of", y , "after", x , " miliseconds is " , result)