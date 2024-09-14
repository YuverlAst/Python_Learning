#找最小公倍数递归方案一:从一开始一个一个找(和遍历一样)
def lcm(a,b,c=1):
    if a*c % b != 0:
        return lcm(a,b,c+1)
    else:
        return a*c
test_cases = [(4,8),(35,42),(5,7),(20,10)]
for case in test_cases:
    print("lcm of {} & {} is {}".format(*case,lcm(*case)))

#找最小公倍数递归方案二:将所有公因子取出并乘以两数的最简式
def lcm1(a,b):
    for i in range(2,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            return i * lcm1(a//i,b//i)
    else:
        return a*b
test_cases1 = [(4,8),(5,7),(24,16),(35,42)]
for case in test_cases1:
    print("lcm of {} and {} is {}".format(*case,lcm1(*case)))

#找最大公约数递归方案:辗转相除法
def gcd(a,b):
    if a == b:
        return a
    elif a-b > b:
        return gcd(a-b,b)
    else:
        return gcd(b,a-b)
test_cases2 = [(35,14),(88,66),(5,4),(20,10)]
for case in test_cases2:
    print("gcd of {} and {} is {}".format(*case,gcd(*case)))

#找最大公约数非递归方案:从一开始一个一个找更大的公因子
def gcd1(a,b):
    if a != 0 and b != 0:
        if a > b:
            a,b = b,a
        if b%a == 0:
            return a
        gcd_list = []
        for i in range(1,a):
            if b % i == 0 and a % i == 0:
                gcd_list.append(i)
        return max(gcd_list)
    else:
        print("Number is wrong!!!")
test_cases2 = [(35,14),(88,66),(5,4),(20,10)]
for case in test_cases2:
    print("gcd of {} and {} is {}".format(*case,gcd(*case)))