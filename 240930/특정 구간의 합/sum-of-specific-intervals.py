n, m = map(int, input().split())
nList = list(map(int, input().split()))
mList = []
for i in range(m):
    a,b = map(int, input().split())
    print(sum(nList[a-1:b]))