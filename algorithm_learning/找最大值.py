"""

分治:将数组分为左右两个部分,当数组长度小于等于2时使用内置的max函数返回最大值
归并:将返回值比较并返回左右两部分返回值中较大的一个

"""
def get_max(max_list):
    return max(max_list)

def solve2(init_list):
    n = len(init_list)
    if n <= 2:
        return get_max(init_list)
    left_list,right_list = init_list[:n//2],init_list[n//2:]
    left_max,right_max = solve2(left_list),solve2(right_list)
    return get_max([left_max,right_max])

if __name__ == '__main__':
    test_list = [12,2,23,45,67,3,2,4,45,63,24,23]
    print("最大值:",solve2(test_list))