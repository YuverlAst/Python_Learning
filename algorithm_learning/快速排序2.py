"""

方案二:使用列表进行排序

"""
#第一版
def quick_sort1(a):
    if a == []:
        return a
    else:
        key = a[0]
        left = [i for i in a[1:] if i < key]
        right = [k for k in a[1:] if k > key]
        return quick_sort1(left) + [j for j in a if j == key] + quick_sort1(right)

#第二版
def partition(a,low,high):
    pivotkey = a[high]
    print(pivotkey)
    while low < high:
        while (low < high and a[low] <= pivotkey):
            low += 1
        a[low],a[high] = a[high],a[low]
        while (low < high and a[high] >= pivotkey):
            high -= 1
        a[low],a[high] = a[high],a[low]
    print(a)
    return low

def quick_sort2(a,low,high):
    if low < high:
        pivot = partition(a,low,high)
        quick_sort2(a,low,pivot-1)
        quick_sort2(a,pivot+1,high)

a = [2,8,7,1,3,5,6,4]
quick_sort2(a,0,7)
print(a)