"""

方案二:使用分治的方法将问题分为长度为2的小组后取得最大最小值,返回并比较出最大最小值

"""
def selectMaxMin(arr,low,high):
    if high - low <= 1:
        maxx,minn = max(arr[low],arr[high]),min(arr[low],arr[high])
        return maxx,minn
    max_L,min_L = selectMaxMin(arr,low,low + (high-low)//2)    
    max_R,min_R = selectMaxMin(arr,low + (high-low)//2 + 1,high)
    return max(max_R,max_L),min(min_R,min_L)

if __name__ == '__main__':
    arr = [1,3,-1,4,9,5,2]
    print(selectMaxMin(arr,0,6))