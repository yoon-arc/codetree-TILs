student_number = int(input())
student = [ [] for _ in range(student_number + 1) ] 
num = 0
count = 0

for i in range(1, student_number + 1):
    student[i] += map(int, input().split())
        #student[i] = map(int, input().split()) => object map 오류 뜸
            #student[i].append( map(int, input().split()) ) => object map 오류 뜸

for i in range(1, student_number + 1):
    num = 0
    while student[i] :
        num += student[i].pop()
                                
    else:
        avg = num/4
        student[i].append(avg)
        if student[i][0] >= 60:
            print("pass")
            count += 1
        else:
            print("fail")
print(count)