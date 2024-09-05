N = int(input())
x = 0

while True:
    if(N==0):
        break
    N //= 2
    x += 1

print(x-1)