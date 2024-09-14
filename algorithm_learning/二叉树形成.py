class Node():
    
    def __init__(self,data = None):
        self._data = data
        self._left = None
        self._right = None

    def set_data(self,data):
        self._data = data
    
    def get_data(self):
        return self._data
    
    def set_left(self,node):
        self._left = node

    def get_left(self):
        return self._left
    
    def set_right(self,node):
        self._right = node

    def get_right(self):
        return self._right

"""

line32的语句用于测试模块的功能并防止此模块被调用时其下的语句被运行
__name__为python的内置变量

"""

if __name__ == '__main__':
    root_node = Node('a')
    left_node = Node('b')
    right_node = Node('c')
    root_node.set_left(left_node)
    root_node.set_right(right_node)

    print(root_node.get_data(),root_node.get_left().get_data(),root_node.get_right().get_data())