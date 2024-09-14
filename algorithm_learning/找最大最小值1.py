"""

方案一:将数据拆分成两个一组,每组排出大小后遍历查找最大值和最小值

"""
class MaxMin():
    def __init__(self):
        self.max = None
        self.min = None

    def getMax(self):
        return self.max
    
    def getMin(self):
        return self.min
    
    def GetmaxAndmin(self,arr):
        if arr == None:
            print("参数不合法")
            return
        lens = len(arr)
        self.max = arr[0]
        self.min = arr[0]
        #两两分组并组内排序
        i = 0
        while i < (lens-1):
            if arr[i] < arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = arr[i]
            i += 2
        #在每组左侧查找最小值
        self.min = arr[0]
        i = 2
        while i < lens:
            if arr[i] < self.min:
                self.min = arr[i]
            i += 2
        #在每组右侧找最大值
        self.max = arr[1]
        i = 3
        while i < lens:
            if arr[i] > self.max:
                self.max = arr[i]
            i += 2
        #以上对前偶数项进行处理,以下考虑奇数项数情况的最后一项    
        if lens % 2 == 1:
            if arr[lens - 1] < self.min:
                self.min = arr[lens - 1]
            if arr[lens - 1] > self.max:
                self.max = arr[lens - 1]

if __name__ == '__main__':
    array = [7,3,19,40,4,7,1]
    m = MaxMin()
    m.GetmaxAndmin(array)
    print("max = "+str(m.getMax()))
    print("min = "+str(m.getMin()))