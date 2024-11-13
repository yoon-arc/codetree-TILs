N = int(input())
cows = list(map(int, input().split()))
count = 0

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            A,B,C = cows[a],cows[b],cows[c]
            if A<=B<=C:
                count += 1


print(count)