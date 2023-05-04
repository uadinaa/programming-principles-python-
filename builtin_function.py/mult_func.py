def mult(num):
    x = 1
    for i in num:
        x*=i
    return x
    
num = (1, -9 ,2, 3, 4, 5)
y = mult(num)
print(y)