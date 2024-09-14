class Node():
    def __init__(self,data = None,left = None,right = None):
        self._data = data
        self._left = left
        self._right = right

#先序遍历
def pro_order(tree):
    if tree == None:
        return False
    print(tree._data)
    pro_order(tree._left)
    pro_order(tree._right)

#后序遍历
def pos_order(tree):
    if tree == None:
        return False
    pos_order(tree._left)
    pos_order(tree._right)
    print(tree._data)

#中序遍历
def mid_order(tree):
    if tree == None:
        return False
    mid_order(tree._left)
    print(tree._data)
    mid_order(tree._right)

#层次遍历
def row_order(tree):
    queue = []
    queue.append(tree)                  #读入二叉树数据
    while True:
        if queue == []:                 #遍历完后queue上的二叉树数据已经被全部输出并清空
            break
        print(queue[0]._data)           #输出最上一行数据
        first_tree = queue[0]           #将最上一行数据读出并将左右分支分开追加至queue最后,保证所有数据被线性输出
        if first_tree._left != None:
            queue.append(first_tree._left)
        if first_tree._right != None:
            queue.qppend(first_tree._right)
        queue.remove(first_tree)        #将最上一行数据清除

if __name__ == '__main__':
    tree = Node('A',Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))
    
    print("pro:\n")
    pro_order(tree)
    print("mid:\n")
    mid_order(tree)
    print("pos:\n")
    pos_order(tree)
    #print("row:\n")
    #row_order(tree)