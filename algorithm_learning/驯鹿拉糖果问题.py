from __future__ import division

input_a = input(u'箱数:')
max = input(u'最大承受重量:')

list_c = []
list_z = []

for i in range(1,int(input_a)+1):
    input_c = input('第' + str(i) + '箱的总价值:')      #此箱价值
    input_d = input('第' + str(i) +'箱的总重量:')       #此箱重量
    avg = round(int(input_c) / int(input_d),1)         #单位价值
    list_c.append(avg)                                 #对单位价值进行排序
    list_z.append([int(input_d),avg,0])                #分别为总重量,单位价值,是否被取走

list_c.sort(reverse = True)     #降序排序
sum = [0,0]             #前一个数据用来存储直接拿取全部当前物品后的总重量,后一个备份以备超重后重新计算
overWeight = 0          #判断是否超重
value = 0               #总价值

for i in range(len(list_c)):
    for j in range(len(list_z)):
        if overWeight == 0:
            if(list_c[i] == list_z[j][1] and list_z[j][2] == 0):
                sum[1] =sum[0]
                sum[0] += list_z[j][0]              #取走的重量
                v = list_z[j][0]
                if sum[0] >= int(max):              #超重处理方案
                    overWeight = 1
                    tmp = list_z[j][0]
                    while True:                     #计算出剩余的承载量tmp
                        z = sum[1] + tmp
                        if z <= int(max):
                            break
                        tmp -= 1
                    sum[0] = sum[1]
                    sum[0] += tmp
                    v = tmp
                value += list_c[i] * v               
                list_z[j][2] = 1

print("取走的价值为:",value)