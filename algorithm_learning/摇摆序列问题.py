"""

贪心算法分析:
寻找最大的摆动子序列

"""
class Solution():
    def greedy(self,num):
        if len(num) == 2:
            return num
        BEGIN = 0
        UP = 1
        DOWN = 2
        STATE = BEGIN
        max_length = 1
        for i in range(1,len(num)):
            if STATE == BEGIN:
                if num[i] > num[i-1]:
                    STATE = UP
                    max_length += 1
                elif num[i] < num[i-1]:
                    STATE = DOWN
                    max_length += 1
            if STATE == UP:
                if num[i] < num[i-1]:
                    STATE = DOWN
                    max_length += 1
            if STATE == DOWN:
                if num[i] > num[i-1]:
                    STATE = UP
                    max_length += 1
        return max_length
    
if __name__ == '__main__':
    s = Solution()
    g = [1,17,5,10,13,15,10,5,16,8]
    result = s.greedy(g)
    print(result)