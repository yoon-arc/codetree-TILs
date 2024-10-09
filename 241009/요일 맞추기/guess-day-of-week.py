m1, d1, m2, d2 = map(int, input().split())
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 두 날짜 사이의 일수 차이 계산
def calculate_day_difference(m1, d1, m2, d2):
    # 두 날짜가 같은 월일 경우
    if m1 == m2:
        return d2 - d1
    # 두 날짜가 다른 월일 경우
    elif m1 < m2:
        return (months[m1] - d1) + sum(months[m1+1:m2]) + d2
    else:  # m1 > m2
        return -((months[m2] - d2) + sum(months[m2+1:m1]) + d1)

# 기준 날짜에서 두 번째 날짜까지의 일수 차이
day_difference = calculate_day_difference(m1, d1, m2, d2)

# 요일 계산 (기준 날짜는 월요일)
getDay = (day_difference % 7 + 7) % 7  # 음수를 방지하기 위해 + 7

# 결과 출력
print(days[getDay])