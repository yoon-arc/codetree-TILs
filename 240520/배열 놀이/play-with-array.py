n, q = map(int, input().split())
num_list = list(map(int, input().split()))

for _ in range(q):
    case = list(map(int, input().split()))
    Q = case.pop(0)

    if Q == 1:
        num = case.pop(0)
        print(num_list[num-1])
                
    if Q == 2:
        num = case.pop(0)
        if num in num_list:
            print(num_list.index(num)+1)
        elif num not in num_list:
            print(0)
        
    if Q == 3:
        num = case.pop(0)
        s_case = case.pop(0)
        Q3 = num_list[num-1:s_case]
        for i in Q3:
            print(i, end = ' ')