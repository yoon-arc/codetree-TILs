number = list(map(int,input().split()))

for i in range(len(number)):
    
    if 999 in number:
        number.sort
        number.pop()
        print(max(number), min(number))
        break
    if -999 in number:
        umber.sort
        number = number[1:]
        print(max(number), min(number))
        break