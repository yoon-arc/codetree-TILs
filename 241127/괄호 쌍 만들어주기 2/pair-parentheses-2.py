#배열에서 [i]와 [i+1]가 둘 다 == '('인지
#그렇다면 [i+2]부터 끝까지 돌면서 j와 j+1이 '))'인지
#맞다면 카운트

braces = list(input())
count = 0
#첫 번째 반복문 '(','('를 찾기 위한
for i in range(len(braces)):
    if braces[i] == '('and braces[i+1] == '(':
        for j in range(i+3,len(braces)):
            if braces[j-1] == ')'and braces[j] == ')':
                count += 1

print(count)