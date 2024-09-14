"""

使用贪心算法:
将总面额分解为局部小面额问题寻找最优解,然后从总面额中去除已解决的局部找零,考虑下一个解

用当下未使用的最大面额尽可能补充找零,减去已找零,继续对下一个最大面额考虑是否形成局部解,重复上述步骤

"""
def main():
    d = [0.01,0.02,0.05,0.1,0.2,0.5,1.0]            #所有面值
    d_num = []
    s = 0
    
    tmp = input("请输入各个面值硬币的数量:")
    d_num0 = tmp.split(" ")
    for i in range(0,len(d_num0)):
        d_num.append(int(d_num0[i]))
        s += d_num[i] * d[i]
    
    sum = float(input("请输入需要找的总额"))
    if sum > s:
        print("不够找零!")
        return 0
    
    i = 6
    while i > 0:
        if sum > d[i]:
            n = int(sum / d[i])
            if n > d_num[i]:
                n = d_num[i]
            sum -= n * d[i]
            print("用了%d个%f硬币"%(n,d[i]))
        i -= 1
    
if __name__ == '__main__':
    main()