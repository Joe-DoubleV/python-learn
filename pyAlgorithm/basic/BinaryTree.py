class BinaryTree:
    """docstring for BinaryTree"""
    def __init__(self, rootObj):
        
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def midorder(self):
        if self.leftChild:
            self.leftChild.preorder()
        print(self.key)        
        if self.rightChild:
            self.rightChild.preorder()
    def aforder(self):
        if self.leftChild:
            self.leftChild.preorder()
               
        if self.rightChild:
            self.rightChild.preorder()

        print(self.key) 

if __name__ == '__main__':
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.insertLeft('d')
    r.insertLeft('e')

    print(r.getRootVal())
    # print(r.getLeftChild().getRightChild().getRootVal())
    print(r.getRightChild().getRootVal())
    r.midorder()
