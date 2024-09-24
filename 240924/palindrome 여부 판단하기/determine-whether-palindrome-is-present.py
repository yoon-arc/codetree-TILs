def isPalindrome(A):
    for i in range(0,len(A)//2):
        if A[i] == A[-i]:
            continue
        else:
            return 'No'
    return 'Yes'

A = input()
print(isPalindrome(A))