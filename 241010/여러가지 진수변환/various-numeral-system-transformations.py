N, B = input().split()
B = int(B)
N = int(N)
result = ""

# N을 B진수로 변환
while N > 0:
    result = str(N % B) + result
    N //= B

print(result)