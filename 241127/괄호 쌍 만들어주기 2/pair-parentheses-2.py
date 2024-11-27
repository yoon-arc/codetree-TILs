#배열에서 [i]와 [i+1]가 둘 다 == '('인지
#그렇다면 [i+2]부터 끝까지 돌면서 j와 j+1이 '))'인지
#맞다면 카운트

braces = list(input())
count = 0

#첫 번째 반복문 '('를 찾기 위한
for i in range(len(braces)-1):
    #시작 점을 기준으로 하나하나씩 둘러보기
    for j in range(i+1, len(braces)-1):
        if braces[i] == '(' and braces[i+1] == '(' and braces[j]==')'and braces[j+1]==')':
            count += 1

print(count)