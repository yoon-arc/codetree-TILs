a, b = map(int, input().split())
def getNum(a,b):
    if a>b:
        return print(a*2, b+10)
    else:
        return print(a+10, b*2)
getNum(a,b)