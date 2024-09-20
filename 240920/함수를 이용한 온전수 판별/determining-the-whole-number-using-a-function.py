a, b = map(int, input().split())
count = 0

def perfectNum(n):
    if n%2 == 0:
        return False 
    if n%10 == 5:
        return False
    if n % 3 == 0 and n%9 != 0:
        return False
    return True

    
for i in range(a, b+1):
    if perfectNum(i):
        count += 1
    

print(count)