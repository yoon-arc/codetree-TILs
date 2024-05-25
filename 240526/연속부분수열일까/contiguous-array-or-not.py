num1, num2 = map(int, input().split())
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
check = [False for _ in range(num1)]
new_list = []



for i in range(num1):
    if n1[i] in n2:
        new_list.append(n1[i])
        check[i] = True

length = 0
for i in check:
    if i == False:
        length = 0
    if i == True:
        length += 1
        if length == len(n2):
            print("Yes")
            break


if length != len(n2):
    print("No")