"""

方案二:分解问题,解决后合并

"""
def is_in_list(init_list,el):
    return [False,True][init_list[0] == el]

def solve(init_list,el):
    n = len(init_list)
    if n == 1:
        return is_in_list(init_list,el)
    left_list,right_list = init_list[:n//2],init_list[n//2:]
    res = solve(left_list,el) or solve(right_list,el)
    return res

if __name__ == '__main__':
    test_list = [12,2,23,45,67,3,2,4,45,63,24,23]
    print(solve(test_list,45))
    print(solve(test_list,5))