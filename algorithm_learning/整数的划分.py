#n为被划分数,m为划分的最大加数
def intDivide(n,m):
    if n == 1 or m == 1:
        return 1
    if n < m:
        return intDivide(n,n)
    if n == m:
        return intDivide(n,m-1) + 1
    if n > m and m > 1:
        return intDivide(n-m,m) + intDivide(n,m-1)
    return 0
print(intDivide(12,2))