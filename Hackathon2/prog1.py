def isPalindrome(s):
    return s == s[::-1]
 
s = input()
ans = isPalindrome(s)
 
if ans:
    print("1")
else:
    print("0")