N = int(input())
words = list(input())
cases = 0
#C찾기
for c in range(N):
    for o in range(c+1, N):
        for w in range(o+1, N):
            if words[c] == 'C' and words[o] == 'O' and words[w] == 'W':
                cases += 1

print(cases)
#O찾기
#W찾기