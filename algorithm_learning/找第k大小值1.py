"""

选取枢纽元素,将所有元素分为大于枢纽/小于枢纽两组,如果小于枢纽一组的个数等于需要的k-1,则枢纽元素为第k大元素
否则以枢纽元素为中点进行分治,继续寻找符合要求的元素

"""
def partition(seq):
    pi = seq[0]             #枢纽元素为被传入数组的第一个元素
    lo = [x for x in seq[1:] if x <= pi]        #第一组
    hi = [x for x in seq[1:] if x > pi]         #第二组
    return lo,pi,hi

def select(seq,k):          #被传入数组及寻找的大小序
    lo,pi,hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m <= k:
        return select(hi,k-m-1)
    else:
        return select(lo,k)
    
if __name__ == '__main__':
    seq = [3,4,1,6,3,7,9,13,93,0,100,1,2,2,3,3,2]
    print(select(seq,3))
    print(select(seq,1))