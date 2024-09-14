"""

找出五位数"算法描述题":算法描述题 * 算 = 题题题题题题

"""
for i in range(10000,99999):
    for j in range(1,10):
        if i * j % 111111 == 0:
            if len(set(str(i))) == 5:
                if str(j) == str(i)[0]:
                    print("找到满足条件的数:{}\n".format(i))