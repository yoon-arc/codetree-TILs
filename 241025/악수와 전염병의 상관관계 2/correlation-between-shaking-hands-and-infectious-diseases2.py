def getInfection(N, K, P, T):
    developers = [0] * N
    developers_check = [0] * N
    developers[P-1] = 1  # 최초 감염자 설정
    infection_log = [tuple(map(int, input().split())) for _ in range(T)]
    infection_log.sort()
    
    for t, x, y in infection_log:

        #감염 여부를 확인하고 일단 악수 횟수 증가
        if developers[x-1]:
            developers_check[x-1] += 1
        if developers[y-1]:
            developers_check[y-1] += 1

        
        # 둘 중 하나만 감염이 된 상태일 때
        if developers[x-1] and developers_check[x-1] <= K and not developers[y-1]:
            developers[y-1] = 1
            
        if developers[y-1] and developers_check[y-1] <= K and not developers[x-1]:
            developers[x-1] = 1
        


    print(*developers, sep="")

N, K, P, T = map(int, input().split())
getInfection(N, K, P, T)