# 数据结构:
#   内置数据结构:  list...
#   外置:  栈/队列....   两种基本数据结构


# 栈: 先进后出, 后进先出
#   Stack()创建一个空栈  
#   push(item)  将一个元素添加到栈的顶端  ---> 入栈
#   pop()  将栈顶端的数据移除 
#   peek() 返回栈顶元素 
#   isEmpty()  检查栈是否为空    ---> 返回是布尔类型
#   size() 返回栈中元素的数目


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
        
    
        
# 创建栈
s = Stack()
# 判断栈是否为空
print(s.isEmpty())
# 加入数据
s.push(666)
print(s.isEmpty())
# 返回栈中元素的个数
print(s.size())
s.pop()
print(s.size())



