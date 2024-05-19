caseA = 0
caseB = 0
caseC = 0
caseD = 0


for i in range(3):
    Symp, Temp = input().split()

    if Symp == 'Y' and int(Temp) >= 37:
        caseA += 1

    if Symp == 'N' and int(Temp) >= 37:
        caseB += 1

    if Symp == 'Y' and int(Temp) < 37:
        caseC += 1

    if Symp == 'N' and int(Temp) < 37:
        caseD += 1


if caseA >= 2:
    print(f"{caseA} {caseB} {caseC} {caseD} E")

else:print(f"{caseA} {caseB} {caseC} {caseD}")