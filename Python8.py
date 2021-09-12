#8. Write a program to find Armstrong number or not.

num = int(input("Enter number: \n"))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")

else:
    print(num, "is not an Armstrong number")

