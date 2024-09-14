import itertools
import copy

a = int(input("请输入第一个数字:"))
b = int(input("请输入第二个数字:"))
c = int(input("请输入第三个数字:"))
d = int(input("请输入第四个数字:"))
inputlist = [a,b,c,d]
listAll = []                #储存列表的所有排列组合
listSignIndex = []          #储存符号的顺序
listSign = []               #储存符号
listSet = list(itertools.permutations(inputlist,4))     #储存列表的所有排列组合
for i in listSet:                                       #将排列组合从元组转换为列表
    listAll.append(list(i))

def changeIndexToSign():
    for i in listSignIndex:
        if i == 0:
            listSign.append('+')
        elif i == 1:
            listSign.append('-')
        elif i == 2:
            listSign.append('*')
        elif i == 3:
            listSign.append('/')
last = []
def start():
    global last
    while 1:
        for list1 in listAll:
            val = list1[0]
            last = copy.deepcopy(list1)
            for i in range(4):
                if i == 0:
                    val += list1[1]
                elif i == 1:
                    val -= list1[1]
                elif i == 2:
                    val *= list1[1]
                elif i == 3:
                    val /= list1[1]
                val2 = val          #保存此种组合下第 1,2 位元素运算的结果
                for j in range(4):
                    if j == 0:
                        val += list1[2]
                    elif j == 1:
                        val -= list1[2]
                    elif j == 2:
                        val *= list1[2]
                    elif j == 3:
                        val /= list1[2]
                    val1 = val          #保存此种组合下第 1,2,3 位元素运算的结果
                    for k in range(4):
                        if k == 0:
                            val += list1[3]
                        elif k == 1:
                            val -= list1[3]
                        elif k == 2:
                            val *= list1[3]
                        elif k == 3:
                            val /= list1[3]
                        if val == 24:
                            listSignIndex.append(i)
                            listSignIndex.append(j)
                            listSignIndex.append(k)
                            changeIndexToSign()
                            return
                        else:
                            val = val1
                    val = val2
                val = list1[0]

start()
listSign.append("")
lastStr = "(("
for i in range(4):
    if i == 1 or i == 2:
        lastStr += str(last[i]) + ")" + listSign[i]
    else:
        lastStr += str(last[i]) + listSign[i]
print(lastStr)