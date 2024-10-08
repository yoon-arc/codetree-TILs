a, b, c = map(int, input().split())
day = 11
hour = 11
minu = 11
total = 0

# 목표 시간이 기준 시간보다 앞서는 경우 처리
if a < 11 or (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
    print(-1)
else:
    while True:
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