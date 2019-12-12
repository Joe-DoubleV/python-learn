from Node import Node
class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1 
            current = current.getNext()
        return count

    def add(self,item):
        current = self.head
        previous = None
        
        stop = False

        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else :
                previous = current
                current = current.getNext()
        tem = Node(item)
        if previous is None:
            self.head = tem
            tem.setNext(current)
        else:
            previous.setNext(tem)
            tem.setNext(current)

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
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
    olist = OrderedList()
    olist.add(12)
    olist.add(10)
    olist.add(11)
    olist.printAll()
    print(olist.pop())
