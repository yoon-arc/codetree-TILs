num1, num2 = map(int, input().split())
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
check = [False for _ in range(num1)]
new_list = []


for i in range(num1):
    if n1[i] in n2:
        check[i] = True


length = 0

for i in range(num1):
    if check[i] == False:
        new_list = []
        length = 0
        continue
        
    if check[i] == True:
        length += 1
        new_list.append(n1[i])
        if length == len(n2) and new_list == n2:
            print("Yes")
            break

if length != len(n2):
    print("No")