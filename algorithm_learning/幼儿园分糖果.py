class Solution:
    def foundContentChild(self,ne,re):
        ne = sorted(ne)
        re = sorted(re)
        child = 0
        candy = 0
        while child < len(ne) and candy < len(re):
            if re[candy] >= ne[child]:
                child += 1
            candy += 1
        return child

if __name__ == '__main__':
    ne = [5,10,2,9,15,9]
    re = [6,1,20,3,8]
    s = Solution()
    result = s.foundContentChild(ne,re)
    print(result)