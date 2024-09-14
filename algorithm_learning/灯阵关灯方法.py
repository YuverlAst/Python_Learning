"""

第一行有2^6种按法,可以作为遍历的条件
除第一行外的每一行是否按下均取决于上一行的状态,因此第一行的每一种按法对应的结果是确定的,推导出结果并检验即可

"""
import numpy as np

line = [[0] * 6] * 5
for i in range(5):
    line[i] = input("请输入第{}行:".format(i)).split(",")
    line[i] = list(map(int,line[i]))

#为了保证每个位置的按灯情况计算方法一致,向最上行及最左最右两列增加全0行全0列
puzzle = np.array(line)
zero = np.zeros(6)
puzzle = np.insert(puzzle,0,values = zero,axis = 0)     #向puzzle最上面加入一行0
puzzle = np.insert(puzzle,6,values = zero,axis = 1)     #向puzzle最后一列插入一列0
puzzle = np.insert(puzzle,0,values = zero,axis = 1)     #向puzzle第0列插入一列0

press = np.zeros((6,8))

def guess():
    for r in range(1,5):
        for c in range(1,7):        #由上方灯是否亮决定是否按下下方灯
            press[r+1][c] = (press[r][c] + press[r][c-1] + press[r][c+1] + puzzle[r][c] + press[r-1][c]) % 2
    for c in range(1,7):            #判断最后一行灯是否全部熄灭
        if (press[5][c-1] + press[5][c] + press[5][c+1] + press[4][c]) != puzzle[5][c]:
            return 0
    return 1

def enumeration():                  #对第一行按灯的所有可能性进行遍历
    while guess == 0:               #即前一种第一行的按法错误,则按照二进制方法继续向下一种方法遍历
        press[1][1] += 1
        c = 1
        while (press[1][c] > 1):    #满二进一
            press[1][c] = 0
            c += 1
            press[1][c] += 1
        continue

enumeration()
print("灯的初始状态:\n",puzzle[1:6,1:7])
print("按下结果:\n",press[1:6,1:7])