"""

从第一位开始计算子元素之和,如果当前之和大于最大记录,则更新最大记录,达成局部最优解
如果当前之和为0,则舍弃已求和的全部元素从下一位开始求和

"""
def main():
    s = [12,-4,32,-36,12,6,-6]
    print("定义的列表为:",s)
    s_max,s_sum = 0,0
    for i in range(len(s)):
        s_sum += s[i]
        if s_sum > s_max:
            s_max = s_sum
        elif s_sum < 0:
            s_sum = 0
    print(s_max)

if __name__ == '__main__':
    main()