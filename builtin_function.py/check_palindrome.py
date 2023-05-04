def palindr(arr):
    if arr == arr[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")

arr = input()
palindr(arr)