fib_table = {}

def fib_num(n):
    if n <= 1:
        return n
    if n not in fib_table:
        fib_table[n] = fib_num(n-1) + fib_num(n-2)
    return fib_table[n]                     #为什么line8缩进成为line6条件下的语句后会报错

n = int(input("输入斐波那契数列的第n项:"))
print("斐波那契数列的第" , n , "项是" , fib_num(n))