"""

对有序数组进行二分查找

"""
data = [1,3,6,13,56,123,345,1024,3223,6688]

def dichotomy(min,max,d,n):
    mid = (min+max) // 2
    if mid == 0:
        return 'None'
    elif d[mid] < n:
        print('向右侧找!')
        return dichotomy(mid,max,d,n)
    elif d[mid] > n:
        print('向左侧找!')
        return dichotomy(min,mid,d,n)
    else:
        print('找到了%s'%d[mid])
        return
    
res = dichotomy(0,len(data),data,6688)
print(res)
print("Hello World!")