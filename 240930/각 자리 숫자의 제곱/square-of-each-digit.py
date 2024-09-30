n = int(input())
sum = 0
def recursive(n):
    global sum
    if n == 0:
        return
    recursive(n//10)
    sum += (n%10)**2
recursive(n)
print(sum)