def getInfection(N, K, P, T):
    developers = [0] * N
    developers_check = [0] * N
    developers[P-1] = 1  # 최초 감염자 설정
    infection_log = [tuple(map(int, input().split())) for _ in range(T)]
    infection_log.sort()
    
    for t, x, y in infection_log:
        # x와 y 중 적어도 한 명이 감염 상태일 경우
        if developers[x-1] or developers[y-1]:
            # 둘 중 하나만 감염이 된 상태일 때
            if developers[x-1] and developers_check[x-1] < K and not developers[y-1]:
                developers[y-1] = 1
                developers_check[x-1] += 1
                developers_check[y-1] += 1
            elif developers[y-1] and developers_check[y-1] < K and not developers[x-1]:
                developers[x-1] = 1
                developers_check[y-1] += 1
                developers_check[x-1] += 1
            
            # 둘 다 감염 상태이며 아직 횟수가 안 찼을 때
            elif developers[x-1] and developers[y-1]:
                if developers_check[x-1] < K:
                    developers_check[x-1] += 1
                if developers_check[y-1] < K:
                    developers_check[y-1] += 1
            
            # 둘 다 감염 상태이며 K를 초과한 경우, K만큼만 카운팅
            elif developers[x-1] and developers_check[x-1] >= K:
                developers_check[y-1] += 1
                
            elif developers[y-1] and developers_check[y-1] >= K:
                developers_check[x-1] += 1

    print(*developers, sep="")

N, K, P, T = map(int, input().split())
getInfection(N, K, P, T)