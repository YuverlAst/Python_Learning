"""

方案三:边分组边排序,和方案二逻辑相同,将排序和查找集成在同一个函数中

"""
def selectTopK(arr,low,high,k):
    if low == high and k == 0:
        return arr[0]
    i,j = low,high
    pivotkey = arr[high]
    while i < j:
        while (i < j and arr[i] <= pivotkey):
            i += 1
        arr[i],arr[j] = arr[j],arr[i]
        while (i < j and arr[j] >= pivotkey):
            j -= 1
        arr[i],arr[j] = arr[j],arr[i]
    print("i:",i)
    if k == i:
        return arr[i]
    elif k < i:
        return selectTopK(arr,low,i-1,k)
    else:
        return selectTopK(arr,i+1,high,k)
    
if __name__ == '__main__':
    arr = [1,5,3,4,2,3]
    print(selectTopK(arr,0,5,3))