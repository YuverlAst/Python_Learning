"""

方案四:生成随机校验码对数组进行分治排序,如果排序后位置为k则该校验元素即为第k大小元素

"""
import random

def selectTopK(arr,low,high,k):
    if low == high and k == 0:
        return arr[low]
    m = random.randint(low,high)
    pivotkey = arr[m]
    arr[m],arr[high] = arr[high],arr[m]
    i,j = low,high
    while (i < j and arr[i] < pivotkey):
        i += 1
    arr[i],arr[j] = arr[j],arr[i]
    while (i < j and arr[j] > pivotkey):
        j -= 1
    arr[i],arr[j] = arr[j],arr[i]
    print("i:",i)
    t = i - low - 1
    if t == k:
        return arr[i]
    elif t < k:
        return selectTopK(arr,i+1,high,k-t)
    else:
        return selectTopK(arr,low,i-1,k)
    
if __name__ == '__main__':
    arr = [1,5,3,4,2,3,9]
    print(sorted(arr))
    print(selectTopK(arr,0,6,1))