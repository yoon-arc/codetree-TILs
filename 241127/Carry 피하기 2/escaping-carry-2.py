#참고해서 바꿔본 거


from itertools import combinations 

#계산 함수
def cal_sum(a,b,c):
    #숫자 기본 세팅 해주기
    max_len = max(len(str(a)),len(str(b)),len(str(c)))
    a,b,c = str(a).zfill(max_len), str(b).zfill(max_len), str(c).zfill(max_len)
    #기본 세팅 값
    carry = False
    total_sum = -1
    
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
        
    
# 내 원래 코드
# from itertools import combinations 

# #문자 길이 통일해주는 함수
# def make_even(n,max_len):
#     if len(n) < max_len:
#         n = ('0'*(max_len-len(n))) + n
#     return n

# #확인하는 함수
# def is_the_one(a,b,c,max_len):
#     is_true = True
#     for i in range(max_len):
#         if int(a[i])+int(b[i])+int(c[i]) >= 10:
#             is_true = False
#     return is_true


# #기본 값 받기
# n = int(input())
# nums = [input() for _ in range(n)]
# max_num = -1

# #숫자 확인하기
# for a,b,c in combinations(nums, 3):
#     now_num = -100
#     max_length = max(len(a),len(b),len(c))
    
#     #문자 길이 통일
#     a,b,c = make_even(a,max_length), make_even(b,max_length), make_even(c,max_length)
#     now_num = int(a)+int(b)+int(c) if is_the_one(a,b,c,max_length) else -100
   
#     if now_num > max_num:
#         max_num = now_num
        
# print(max_num) if max_num != -100 else print(-1)

        
        
    
    