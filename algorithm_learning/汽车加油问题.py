def greedy():
    n = 100
    k = 5
    d = [50,80,39,60,40,32]
    num = 0
    for i in range(k):
        #如果有两个加油站之间的距离大于汽车加满油行驶的最大距离,则无法完成行进
        if d[i] > n:
            print("No Solution!")
            return
        
        i,s = 0,0
    while i <= k:
        s += d[i]
        if s >= n:          #仅当局部几站距离之和大于汽车最大行进距离时才进行一次加油.达成局部最优解
            s = d[i]
            num += 1
        i += 1
    print(num)

if __name__ == '__main__':
    greedy()