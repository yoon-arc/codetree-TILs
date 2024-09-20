def cal (a,o,c):
    if o == '+':
        return f"{a} {o} {c} = {int(a)+int(c)}"
    elif o == '-':
        return f"{a} {o} {c} = {int(a)-int(c)}"
    elif o == '/':
        return f"{a} {o} {c} = {int(a)//int(c)}"
    elif o == '*':
        return f"{a} {o} {c} = {int(a)*int(c)}"
    else:
        return False

a, o, c = input().split()
print(cal(a,o,c))