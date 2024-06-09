N = int(input())
M = list(map(int, input().split()))
new_arr = []

for i in M:
    if i not in new_arr:
        new_arr.append(i)
    else:
        while i in new_arr:
            new_arr.remove(i)

if new_arr:
    print(max(new_arr))

else:
    print(-1)