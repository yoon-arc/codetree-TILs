a, b = map(int, input().split())

def getNum(a,b):
    if a<b:
        return print(a*2, b+25)
    else:
        return print(a+25, b*2)
        
getNum(a,b)