"""

方案一:选取分隔元素,将大于和小于分割元素的元素分到左右两组,通过分治实现排序

"""
def quick_sort(n):
    if len(n) < 2:
        return n
    else:
        pivot = n[0]
        left = [x for x in n[1:] if x < pivot]
        right = [x for x in n[1:] if x > pivot]
        return quick_sort(left) + [x for x in n if x == n[0]] + quick_sort(right)
    
print(quick_sort([5,11,3,5,2,8,6,7,3]))