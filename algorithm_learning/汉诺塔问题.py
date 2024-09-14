i = 1

def move(n,mfrom,mto):
    global i
    print("第{}步:将{}号盘子从{} --> {}".format(i,n,mfrom,mto))
    i += 1

def hanoi(n,A,B,C):
    if n == 1:
        move(n,A,C)
    else:
        hanoi(n-1,A,C,B)
        move(n,A,C)
        hanoi(n-1,B,A,C)

try:
    n = int(input("请输入盘子数目:"))
    print("移动情况如下:")
    hanoi(n,'A','B','C')
except ValueError:
    print("请输入一个大于零的整数!")