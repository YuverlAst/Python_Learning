"""

此例通过阶乘展示了递归函数的调用过程

"""

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return n
    else:
        i = factorial(n-1) * n
        print("intermediate result for",n,"*factorial(",n-1,") is:",i)
        return i
    
i = int(input("请输入需要的阶乘:"))
print(factorial(i))