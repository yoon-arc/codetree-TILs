#첫 줄에 두 정수 n, q가 주어짐
#두 번째 줄에 n개의 정수를 입력 받음(리스트)
# 세 번째 줄부터 q개의 줄에 걸쳐 질의를 하나씩. i번째 줄에는 i번째 질의가(??)
#<출력> : 첫 줄부터 q번째 줄에 거렻 q개의 질의에 대한 결과를 한줄에 하나씩

#전부 인덱스 0무시, 인덱스 1부터 시작. 인덱스 값을 어디선가 +1해줘야함.
#질의: 1 : a -> a번째 원소 출력
#2 : b -> n개의 원소 중 값이 b인 애들 찾기. 없으면 0 출력
#3 : s, e -> s번째 원소부터 e까지 공백으로 구분 end=' ' 출력

n, q = map(int, input().split())
num_list = list(map(int, input().split()))

for _ in range(q):
    case = list(map(int, input().split()))
    if len(case) >= 3:
        Q = case.pop(0)
        num = case.pop(0)
        s_case = case.pop(0)

    else:
        Q = case.pop(0)
        num = case.pop(0)
        
   

    if Q == 1:
        print(num_list[num-1])
                
    if Q == 2:
        if num in num_list:
            print(num_list.index(num)+1)
        elif num not in num_list:
            print(0)
        
    if Q == 3:
        Q3 = num_list[num-1:s_case]
        for i in Q3:
            print(i, end = ' ')