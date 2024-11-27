#참고해서 바꿔본 거


from itertools import combinations 

#계산 함수
def cal_sum(a,b,c):
    #숫자 기본 세팅 해주기
    max_len = max(len(str(a)),len(str(b)),len(str(c)))
    a,b,c = str(a).zfill(max_len), str(b).zfill(max_len), str(c).zfill(max_len)
    #기본 세팅 값
    carry = False
    total_sum = 0
    
    for x,y,z in zip(a,b,c):
        if int(x) + int(y) + int(z) >= 10:
            carry = True
            break  # carry가 발생하면 중단
    
    if not carry:
        total_sum = int(a) + int(b) + int(c)
    return total_sum

#기본 값 받기
n = int(input())
nums = [int(input()) for _ in range(n)]
max_num = -1

#숫자 확인하기
for a,b,c in combinations(nums, 3):
    curr_sum = cal_sum(a,b,c)
    if curr_sum > max_num:
        max_num = curr_sum
    
print(max_num)
        
    
    