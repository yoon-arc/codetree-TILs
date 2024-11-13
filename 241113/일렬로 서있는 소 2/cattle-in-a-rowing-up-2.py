import itertools
N = int(input())
cows = list(map(int, input().split()))
count = 0
cowComb = itertools.combinations(cows,3)

for comb in cowComb:
    A,B,C = comb[0],comb[1],comb[2]
    if A<=B<=C and cows.index(A)<cows.index(B)<cows.index(C):
        count +=1

print(count)