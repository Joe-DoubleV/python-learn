class BinHeap():
    """docstring for BinHeap 二叉堆--近似由完全二叉树实现--log(n)的复杂度得到最小值/注意不是排序，可以用于排序复杂度nlog(n) """
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def perUp(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i] ,self.heapList[i//2] = self.heapList[i//2] ,self.heapList[i]
            i = i//2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize +=1
        self.perUp(self.currentSize)


    def minChild(self,i):
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2 + 1   

    def preDown(self,i):
        while i*2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i] ,self.heapList[mc] = self.heapList[mc] ,self.heapList[i]
            i = mc

    def delMin(self):
        reval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.preDown(1)
        return reval

    def buildHeap(self,alist):
        i = len(alist) // 2 
        self.currentSize = len(alist)
        self.heapList = [0]+alist[:]
        while i > 0:
            print(self.heapList,i)
            self.preDown(i)
            i-=1
        print(self.heapList,i)
if __name__ == '__main__':
    hl = BinHeap()
    hl.insert(3)
    hl.insert(7)
    hl.insert(5)
    hl.insert(4)
    hl.insert(2)
    hl2 = BinHeap()
    hl2.buildHeap([3,7,5,4,2])
    print(hl.heapList)
    while hl.currentSize > 0:
        print(hl.delMin())