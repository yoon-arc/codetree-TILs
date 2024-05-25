num1, num2 = map(int, input().split())
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
new_list = []


for i in n2:
    if i in n1:
        start = n1.index(i)
        new_list += n1[start:len(n2)+2]
        break

# len이 같아질 때 까지 append?

# while len(new_list) != len(n2):
#     new_list.pop()


if new_list == n2:
    print("Yes")

else:
    print("No")