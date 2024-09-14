"""

方案一:先判断再查询

"""
def BinarrySearch(arr,key):
    min = 0
    max = len(arr) - 1

    if key in arr:
        while True:
            center = int((min+max)/2)
            if arr[center] > key:
                max = center - 1
            elif arr[center] < key:
                min = center + 1
            elif arr[center]  == key:
                print(str(key) + "在数组的第" + str(center+1) + "个位置")
                return arr[center]
    else:
        print("此数组中没有这个数字")

if __name__ == '__main__':
    arr = [1,6,9,15,26,38,49,57,63,77,81,93]
    while True:
        key = input("请输入您要查找的数字:")
        if key == ' ':
            print("感谢使用!")
            break
        else:
            BinarrySearch(arr,int(key))