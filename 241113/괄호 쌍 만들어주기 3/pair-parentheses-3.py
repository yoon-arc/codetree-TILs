#값을 입력받기
cases = list(input())
#총 경우의 수를 모두 카운트 할 변수
count = 0

#카운트하는 함수
def get_cases(n):
    return cases[n:].count(')')

#for문, (가 나올 때만 함수가 실행되게
for n in range(len(cases)):
    if cases[n] == '(':
        count += get_cases(n)

print(count)