# a, b = map(int, input().split())
# gcd = []
# result = 0

# for i in range(1, 2881):
#     if (1920 % i == 0 and 2880 % i == 0):
#         gcd.append(i)

# for i in range (a, b+1):
#     if i in gcd:
#         result += 1
  
# if result:
#     print(1)
# else:
#     print(0)

a, b = map(int, input().split())
result = 0

for i in range(a, b+1):
    if (1920 % i == 0 and 2880 % i == 0):
        result += 1

if result:
    print(1)
else:
    print(0)