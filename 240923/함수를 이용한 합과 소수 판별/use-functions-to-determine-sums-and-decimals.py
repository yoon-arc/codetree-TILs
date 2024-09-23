def getPrimeNum (a,b):
    numList = []
    count = 0
    #a와 b 사이 소수 구하기
    for i in range(a,b+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            numList.append(i)
    #모든 자릿수의 합이 짝수인지    
    for j in numList:
        if j <100 and ((j//10)+(j%10))%2 == 0:
            count += 1
        elif j == 100:
            count += 1
    return count

a, b = map(int, input().split())
print(getPrimeNum(a,b))