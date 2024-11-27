from itertools import combinations 

#문자 길이 통일해주는 함수
def make_even(n,max_len):
    if len(n) < max_len:
        n = ('0'*(max_len-len(n))) + n
    return n

#확인하는 함수
def is_the_one(a,b,c,max_len):
    is_true = True
    for i in range(max_len):
        if int(a[i])+int(b[i])+int(c[i]) >= 10:
            is_true = False
    return is_true


#기본 값 받기
n = int(input())
nums = [input() for _ in range(n)]
nPr = list(combinations(nums, 3))
max_num = -100

#숫자 확인하기
for a,b,c in nPr:
    now_num = -100
    max_length = max(len(a),len(b),len(c))
    
    #문자 길이 통일
    a,b,c = make_even(a,max_length), make_even(b,max_length), make_even(c,max_length)
    now_num = int(a)+int(b)+int(c) if is_the_one(a,b,c,max_length) else -100
   
    if now_num > max_num:
        # print(now_num)
        max_num = now_num
    # print()
print(max_num) if max_num != -100 else print(-1)

        
        
    
    