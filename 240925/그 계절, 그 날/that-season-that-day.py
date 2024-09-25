def isLeapYear(Y,D):
    if Y%4 == 0 and (Y%100 != 0 or Y%400 == 0):
        if D <30:
            return 'Winter'
        else:
            return -1
    else:
        if D>28:
            return -1
        else:
            return 'Winter'

def isWinter(Y,M,D):
    if M == 2:
        return isLeapYear(Y,D)
    else:
        return 'Winter'
    
def isSpring(M,D):
    if M%2 == 0 and D>30:
        return -1
    else:
        return 'Spring'
    
def isSummer(M,D):
    if M == 6 and D>30:
        return -1
    else:
        return 'Summer'
    
def isFall(M,D):
    if M%2 == 1 and D>30:
        return -1
    else:
        return 'Fall'
    
def getSeason(Y,M,D):
    if M == 12 or (M>=1 and M<=2):
        return isWinter(Y,M,D)       
    elif M>=3 and M<=5:
        return isSpring(M,D)
    elif M >= 6 and M<= 8:
        return isSummer(M,D)
    elif M>=9 and M<=11:
        return isFall(M,D)
    
Y, M, D = map(int, input().split())
print(getSeason(Y,M,D))