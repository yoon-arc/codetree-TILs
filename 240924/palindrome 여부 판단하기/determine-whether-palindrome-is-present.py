def isPalindrome(A):
    return A == A[::-1]

A = input()
if isPalindrome(A):
    print('Yes')
else:
    print('No')