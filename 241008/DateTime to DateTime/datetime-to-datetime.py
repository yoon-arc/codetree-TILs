a, b, c = map(int, input().split())
day = 11
hour = 11
minu = 11
total = 0

while True:
    if a< 11 and b < 11 and c < 11:
        print(-1)
        break
    if day == a and hour == b and minu == c:
        print(total)
        break

    if hour == 24:
        day += 1
        hour = 0
    if minu == 60:
        hour += 1
        minu = 0
    total += 1    
    minu += 1