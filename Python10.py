#10. Write a program to palindrome or not.

def isPalindrome(s):
	return s == s[::-1]
print("Enter s: ")
s = input()
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
