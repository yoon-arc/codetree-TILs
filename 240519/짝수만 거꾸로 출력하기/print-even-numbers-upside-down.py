n = int(input())
nums = list(map(int, input().split()))

while nums:
    number = nums.pop()
    if number % 2 == 0:
        print(number, end=' ')