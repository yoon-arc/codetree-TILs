start_num = int(input())
num = input().split()
num_list = []

#list.count('n')해서 n이 2개 이상이면 remove('n'을 함.)

for i in num:
    if num.count(i) == 1:
        num_list.append(i)


if len(num_list) == 0:
    print(-1)
else:
    print(max(num))