def isPalindrome(A):
    for i in range(1,len(A)//2+1):
        if A[i-1] == A[-i]:
            continue
        else:
            return 'No'
    return 'Yes'
A = input()
print(isPalindrome(A))