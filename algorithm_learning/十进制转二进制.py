def b(n):
    if n // 2 == 0:
        n = str(n)
        return n
    else:
        x = n % 2
        n = n // 2
        s = str(x)
        return b(n) + s
    
n = int(input("请输入一个十进制数:"))
print("转换后:",b(n))