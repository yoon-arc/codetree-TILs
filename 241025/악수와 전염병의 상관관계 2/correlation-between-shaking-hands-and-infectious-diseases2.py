def getInfection(N,K,P,T):
    developers = [0]*N
    developers_check = [0]*N
    developers[P-1] = 1
    infection_log = [tuple(map(int, input().split())) for _ in range(T)]
    infection_log.sort()
    
    
    for t,x,y in infection_log:
        #K번만큼만의 효력이 있음.
        #지금 x가 몇번째 악수인지를 체크해야할듯

        if developers[x-1] or developers[y-1]:
            # 둘 중 하나만 감염이 된 상태일때
            if developers[x-1]and developers_check[x-1]<K and not developers[y-1]:
                developers[y-1] = 1
                developers_check[x-1] += 1
                developers_check[y-1] += 1
            elif developers[y-1]and developers_check[y-1]<K and not developers[x-1]:
                developers[x-1] = 1
                developers_check[x-1] += 1
                developers_check[y-1] += 1
            # 둘 다 감염 상태이며 아직 횟수가 안찼을 때
            elif developers[x-1]and developers_check[x-1]<K and developers_check[y-1]<K:
                developers_check[x-1] += 1
                developers_check[y-1] += 1
            elif developers[y-1]and developers_check[y-1]<K and developers_check[x-1]<K:
                developers_check[x-1] += 1
                developers_check[y-1] += 1
                
            # 둘 다 감염 상태일 때
            else:
                if developers_check[x-1] < K:
                    developers_check[x-1] += 1
                if developers_check[y-1] < K:
                    developers_check[y-1] += 1
                
            
            
            
            
        
    print(*developers, sep="")


N, K, P, T = map(int, input().split())
getInfection(N,K,P,T)