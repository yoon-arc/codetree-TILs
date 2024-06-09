N = int(input())
M = list(map(int, input().split()))
new_arr = set(M)
countnum = 0

for i in new_arr:
    countnum = M.count(i)
    if countnum > 1:
        while i in M:
            M.remove(i)


if M:
    print(max(M))
else:
    print(-1)