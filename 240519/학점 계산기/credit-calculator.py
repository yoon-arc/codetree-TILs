N = int(input())
sum = 0
avg = 0
score = list(map(float, input().split()))

for i in score:
    sum += i

avg = sum/N

if avg >= 4.0:
    print(f"{avg:.1f}\nPerfect")

elif avg < 4.0 and avg >= 3.0:
    print(f"{avg:.1f}\nGood")

else:
    print(f"{avg:.1f}\nPoor")