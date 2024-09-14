"""

贪心算法分析:
将各个活动以结束时间从小到大排序,优先选择结束时间最早的活动进行

证明此问题可以由贪心算法得到最优解:
若最优解A以活动1开始,由于以活动1开始具有贪心算法特征,则此情况为贪心算法
若最优解A以活动开始,则另设解B = A并{1}-{k},显然为贪心算法得解
由于活动1的结束时间小于活动k,故解B仍成立,且解B的大小等于解A,也为最优解
综上,贪心算法计算出的解一定为最优解

"""
"""

方案一:快速排序

"""
class task():
    def __init__(self,name,s,f):
        self.name = name
        self.s = s
        self.f = f

    def __str__(self):
        return "['%s',%d,%d]" % (self.name,self.s,self.f)
    
    def __repr__(self):
        return self.__str__()


def quick_sort(list,begin,end):
    if begin < end:
        i,j = begin,end
        base = list[begin]
        while i < j:
            while i < j and list[j].f >= base.f:
                j -= 1
            list[i],list[j] = list[j],list[i]
            while i < j and list[i].f <= base.f:
                i += 1
            list[i],list[j] = list[j],list[i]
        list[i] = base
        quick_sort(list,begin,i-1)
        quick_sort(list,j+1,end)
    return list

def get_max(list):                              #利用两个列表:一个存放排序后的活动,一个存放已选择的活动
    job_schedule = []
    num = len(list)
    for i in range(num):
        if not job_schedule:                    #第一个活动选择排序后的活动一
            job_schedule.append(list[i])
        elif job_schedule[-1].f <= list[i].s:
            job_schedule.append(list[i])
    return job_schedule

if __name__ == '__main__':
    joblist = [task('1', 3, 5), task('2', 1, 4), task('3', 0, 6), task('4', 3, 8), task('5', 5, 7), task('6', 6, 10),
               task('7', 5, 9), task('8', 8, 11), task('9', 2, 13), task('10', 8, 12)]
    sort_list = quick_sort(joblist,0,len(joblist)-1)
    print(get_max(sort_list))