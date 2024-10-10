a, b = map(int, input().split())
n = input()
# a진수로 표현된 숫자 n
# b는 바꿔야하는 진수

def getNum(n):
    count = 0
    for i in range(len(n)):
        count += int(n[i])*(a**(len(n)-i-1))
    return count

def changeNum(c):
    nums = []
    while c >= b:
        now = c%b
        c = c//b
        nums.append(now)
        
    nums.append(c)
    return nums[::-1]
    
print(*changeNum(getNum(n)), sep="")