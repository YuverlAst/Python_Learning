"""

方案二:使用快速排序算法每进行一次排序确定一次已确定大小序的index元素是否就是第k大小元素

"""
def partition(arr,low,high):
    pivot = arr[low]
    while low < high:
        while (arr[low] < pivot and low < high):
            low += 1
        while (arr[high] > pivot and low < high):
            high -= 1
        tmp = arr[low]
        arr[low] = arr[high]
        arr[high] = tmp
    return low

def quicksort(arr,low,high):
    if low < high:
        location = partition(arr,low,high)
        quicksort(arr,low,location-1)
        quicksort(arr,location+1,high)

def findkth(arr,low,high,k):
    index = partition(arr,low,high)
    if index == k:
        return arr[index]
    elif index < k:
        return findkth(arr,index+1,high,k)
    else:
        return findkth(arr,low,index-1,k)
    
if __name__ == '__main__':
    pai = [2,3,1,5,4,6]
    print(findkth(pai, 0, len(pai)-1, 5))