import sys
num = list(map(int, input().split()))
min_val = 1000
max_val = -1000

for i in range(len(num)-1):
    if min_val >= num[i]:
        min_val=num[i]

    elif max_val <= num[i] :
        max_val = num[i]


print(max_val, min_val)