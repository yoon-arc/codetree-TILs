def getInfection(N,K,P,T):
    developers = [0]*N
    developers_check = [0]*N
    developers[P-1] = 1
    infection_log = [tuple(map(int, input().split())) for _ in range(T)]
    infection_log.sort()
    
    
    for t,x,y in infection_log:
        #K번만큼만의 효력이 있음.
        #지금 x가 몇번째 악수인지를 체크해야할듯

        if developers[x-1] and developers_check[x-1]<2:
            developers[y-1] = 1
            developers_check[x-1] += 1
            developers_check[y-1] += 1
            
        
    print(*developers, sep="")


N, K, P, T = map(int, input().split())
getInfection(N,K,P,T)