N = int(input())
M = list(map(int, input().split()))
new_arr = []
M.sort()

for i in range(N-1, -1, -1):
    new_arr.append(M[i])


print(new_arr[0], new_arr[1])