class Stack():
    """docstring for Stack"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    for x in range(10):
        
        s.push(x)
        print(s.peek())

    for x in range(10):
        print(s.pop())
        print(s.isEmpty())
        