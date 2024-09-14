"""

方案二:冒泡排序

"""
def bubble_sort(s,f):
    for i in range(len(s)):
        for j in  range(0,len(s)-1):
            if f[j] > f[j+1]:
                f[j],f[j+1] = f[j+1],f[j]
                s[j],s[j+1] = s[j+1],s[j]
    return s,f

def greedy(s,f):                        #两个列表:一个提供排序后的活动,一个存放是否选择每个活动的信息
    a = [True for x in range(len(s))]
    j = 0                               #第一个活动选择排序后的活动一
    for i in range(1,len(s)):           #从排序后的活动中遍历选出符合条件的活动
        if s[i] >= f[j]:
            a[i] = True
            j = i
        else:
            a[i] = False
    return a

if __name__ == '__main__':
    arr = input("请输入每个活动的起止时间:\n").split()
    s = []
    f = []
    for ar in arr:
        ar = ar[1:-1]
        start = int(ar.split(",")[0])
        finish = int(ar.split(",")[1])
        s.append(start)
        f.append(finish)

    s,f = bubble_sort(s,f)
    A = greedy(s,f)

    res = []
    for i in range(len(A)):
        if A[i]:                           #根据选择活动与否形成答案
            res.append('{},{}'.format(s[i],f[i]))
    print(" ".join(res))