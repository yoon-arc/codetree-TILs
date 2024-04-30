number = list(map(int,input().split()))

for i in range(len(number)):
    
    if 999 in number:
        number.pop()
        print(max(number), min(number))
        break
    if -999 in number:
        number = number[1:]
        print(max(number), min(number))
        break