#15. Write a method to find number of even number and odd numbers in an array.

arr = [8, 4, 3, 6, 9, 2]
i = 0
for i in range(0, len(arr)):
    if arr[i]%2 == 0:
        print("Even Number: ", arr[i])
    else:
        print("Odd Number:  ", arr[i])
        i = i +1