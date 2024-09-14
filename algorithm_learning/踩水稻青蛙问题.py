"""

青蛙以不确定的步长和初始点的路径踩过稻田,输入 稻田面积 被踩水稻数量 被踩水稻位置,计算同路径上最多被踩的水稻数
如果从 第一踩 方向 步长 三个因素直接考虑全部枚举,时间复杂度相当高,故从三个角度筛选有可能形成答案路径的方案,减少计算量

将所有被踩点排序,从所有被踩点中选取 第一步 第二步 ,然后计算:
1.第一步之前的一步是否落在田外
2.符合条件1的前提下,按照已有的最多被踩水稻数行进,x方向上是否还落在田内
3.符合条件2的前提下,按照已有的最多被踩水稻数行进,y方向上是否还落在田内
4.符合条件3的前提下,此时步数是否大于已有的最大步数
5.符合条件4的前提下,将最大步数更换为此时的步数

"""
max = 2
RC = input("请输入水稻的行数和列数:").split(' ')
RC = list(map(int,RC))
n = int(input("请输入被踩坏的水稻数目"))
plants = [[0,0]] * n
plant = [0,0]                           #按已确定的第一点和步长对应的下一点坐标
for i in range(n):
    plants[i] = input("请输入第{}个被踩坏的水稻的坐标:".format(i+1)).split(' ')
    plants[i] = list(map(int,plants[i]))

def searchPath(secplant,dx,dy):         #计算并返回此情况下对应踩下的水稻数
    plant[0] = secplant[0] + dx
    plant[1] = secplant[1] + dy
    steps = 2                   
    RC = [6,7]
    while 1 <= plant[0] <= RC[0] and 1 <= plant[1] <= RC[1]:
        if plant not in plants:
            steps = 0
            break
        plant[0] += dx
        plant[1] += dy
        steps += 1
    return steps

plants = sorted(plants)
for i in range(n-2):                    #选取第一点
    for j in range(i+1,n-1):            #选取第二点
        dx = plants[j][0] - plants[i][0]
        dy = plants[j][1] - plants[i][1]
        px = plants[i][0] - dx
        py = plants[i][1] - dy
        if 1 <= px <= RC[0] and 1 <= py <= RC[1]:   #即取到的第一步的上一步落在田里,重取第二点
            continue
        """
        如果从第一步按max步行进对应步长后出田,则由第一步和第二步确定的路径上的被踩水稻数量不会大于max,可以直接舍弃
        由于plants已经排序,在此第一步的情况下,后面所有的第二步均同上情况,可以全部舍弃,考虑下一个第一步的情况
        """
        if plants[i][0] + (max-1)*dy > RC[0]:       
            break

        """
        对第一步的选点更改后需要更新按max步行进对应步长后的位置并判断是否出田
        此时dy可能减小,故可以不断向后寻找第二步位置
        """
        py = plants[i][1] + (max-1)*dy
        if py > RC[1] or py < 1:
            continue

        """
        程序进行到这里说明此时的路径已经符合形成青蛙路径的条件,且踩下的步数大于已有的max
        计算对应的步数即可
        """
        steps = searchPath(plants[j],dx,dy)
        if steps > max:
            max = steps
    if steps == 2:
        max = 0
print(max)