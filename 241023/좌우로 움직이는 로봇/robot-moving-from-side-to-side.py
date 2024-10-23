def compareP(A,B):
    
    #commandA,B에 저장한 튜플 [0]의 값을 각자 합쳐서 기준점이 될 시간을 구하기
    time_A = sum(t for t,d in A)
    time_B = sum(t for t,d in B)
    total_time = max(time_A,time_B)
    
    #인덱스 값
    index_A = index_B = 0
    dir_A = dir_B = 0
    #현재 위치를 저장
    now_A = now_B = 0
    #이전 값을 저장(바로 직전과 비교하기 위해)
    prev_A = prev_B = 0

    #남은 움직임
    move_A = move_B = 0

    #만나는 횟수
    count = 0
    
    #total_time만큼 반복하자
    for i in range(total_time):
    #if문으로 각 리스트가 out of range가 되지 않도록 time_A, time_B와 비교
    
        #A의 경우
        if move_A == 0 and index_A < len(A):
            move_A = A[index_A][0]
            dir_A = 1 if A[index_A][1] == 'R' else -1
            index_A += 1
        #이 부분 때문에 total_time만큼 for문을 돌리는 거임!
        if move_A > 0:
            now_A += dir_A
            move_A -= 1
    
        #B의 경우
        if move_B == 0 and index_B < len(B):
            move_B = B[index_B][0]
            dir_B =  1 if B[index_B][1] == 'R' else -1
            index_B += 1
        #이 부분 때문에 total_time만큼 for문을 돌리는 거임!
        if move_B > 0:
            now_B += dir_B
            move_B -= 1

        if now_A == now_B:
            if prev_A != prev_B :
                count += 1
        

        #이전 위치 값 저장
        prev_A = now_A
        prev_B = now_B

    return count

n, m = map(int, input().split())
#명령을 담음(리스트 길이 아끼기)
commandA = [input().split() for _ in range(n)]
commandB = [input().split() for _ in range(m)]
#갖고 계산할 수 있도록 int로 변환
commandA = [(int(t),d) for t,d in commandA]
commandB = [(int(t),d) for t,d in commandB]

total = compareP(commandA, commandB)
print(total)