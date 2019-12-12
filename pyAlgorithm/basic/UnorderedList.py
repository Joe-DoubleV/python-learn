from Node import Node
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1 
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if current is None:
                break
        if not found:
            print("{} is not in this list".format(item))
            return
        if previous is None:
            self.head = current.getNext()
        else :
            previous.setNext(current.getNext())
    def printAll(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()
    def pop(self):
        current = self.head
        if current is not None:
            self.head = current.getNext()
            return current.getData()
        else :
            return "list is empty"

        
if __name__ == '__main__':
    ulist = UnorderedList()
    ulist.add("a")
    ulist.add("b")
    ulist.add("c")
    print(ulist.size())
    print(ulist.remove("b"))
    print(ulist.size())
    print(ulist.remove("b"))
    print(ulist.search("a"),ulist.search("b"),ulist.search("c"))
    ulist.printAll()
    print(ulist.pop())
    ulist.printAll()
    print(ulist.pop())
    ulist.printAll()
    print(ulist.pop())
    ulist.printAll()
