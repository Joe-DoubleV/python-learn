class TreeNode:
    """docstring for TreeNode"""
    def __init__(self, key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.height = 0
        self.balanceFactor = 0
    def __str__(self):
        return str(self.key) + "/" + str(self.height) + "/" + str(self.balanceFactor)

    def __iter__(self):
        if self:
            if self.getLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.getRightChild():
                for elem in self.rightChild:
                    yield elem
    def max_children_height(self):
        if self.leftChild and self.rightChild:
            return max(self.leftChild.calHeight(), self.rightChild.calHeight())
        elif self.leftChild and not self.rightChild:
            return self.leftChild.calHeight()
        elif not self.leftChild and  self.rightChild:
            return self.rightChild.calHeight()
        else:
            return -1
    def calHeight(self):
        self.height = self.max_children_height() +1
        return self.height

    def calBalanceFactor (self):
        self.calHeight()
        self.balanceFactor = (self.leftChild.height if self.leftChild else -1) - (self.rightChild.height if self.rightChild else -1)
        # return self.balanceFactor
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.rightChild or self.leftChild)
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    def replaceNodeData(self,key,val,lc,rc):
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.getLeftChild():
            self.leftChild.parent = self
        if self.getRightChild():
            self.rightChild.parent = self
    def findSuccessor(self):            #   寻找后继节点
        succ = None
        if self.getRightChild():
            succ = self.rightChild.finMin()
        else:           # 在目前 "小节点在左，大节点在右的"二叉树中，不会出现这中情况
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    def finMin(self):           #   找到（子）树中最小的节点----左树
        current = self
        while current.getLeftChild():
            current = current.leftChild
        return current
    def splitMinOut(self):      #   摘除节点
        if self.isLeaf():       #   直接摘除叶节点
            if self.isLeftChild():
                self.parent.leftChild = None
                self.parent.calBalanceFactor()
            else :
                self.parent.rightChild = None
                self.parent.calBalanceFactor()
        elif self.hasAnyChildren():
            if self.getRightChild():    #   如果有右子树            
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
                self.parent.calBalanceFactor()
            else :      #   如果没有右子树，反之一定有左子树，但是，摘除找到的最小节点不会有这种情况，最小节点一定没有左子树）
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent

class BinarySearchTree:
    """docstring for BinarySearchTree"""
    def __init__(self):        
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):                 #迭代
        return self.root.__iter__()
    def __setitem__(self,k,v):          #索引赋值   myTree[0] = 'red'
        self.put(k,v)
    def __getitem__(self,k):            #索引  sth = myTree[0] 
        return self.get(k)
    def __contains__(self,key):           # in
        if self._get(key,self.root):
            return True
        else:
            return False
    def __delitem__(self,key):              # del myTree[0]
        self.delete(key)
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.getLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent = currentNode)
        else:
            if currentNode.getRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent = currentNode)
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key :
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    def delete(self,key):        
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove :
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('error,key not in tree')
        elif self.size == 1 and self.root.key == key :
            self.root = None
            self.size = 0
        else :
            raise  KeyError('error,key not in tree')    
    def remove(self,currentNode):           #   删除节点
        if currentNode.isLeaf():        #叶节点，直接删
            if currentNode.isLeftChild() :      
                currentNode.parent.leftChild = None
            else :
                currentNode.parent.rightChild = None 
        elif currentNode.hasBothChildren():     #   左右子树都存在
            succ = currentNode.findSuccessor()  #   找到后继节点：大于本节点的最小节点
            succ.splitMinOut()  #   摘除节点
            #   重新赋给原来位置的节点，只需要key，value，其他位置（父子）关系不变
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else :      #   只有一个子树存在
            if currentNode.getLeftChild():      #   有左子树
                if currentNode.isLeftChild():       #   自己是左子树
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():    #   自己是右子树
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:               #   自己是root
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild)
            else :      #   有右子树
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild)

class AVL_BinarySearchTree:
    """docstring for BinarySearchTree"""
    def __init__(self):        
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):                 #迭代
        return self.root.__iter__()
    def __setitem__(self,k,v):          #索引赋值   myTree[0] = 'red'
        self.put(k,v)
    def __getitem__(self,k):            #索引  sth = myTree[0] 
        return self.get(k)
    def __contains__(self,key):           # in
        if self._get(key,self.root):
            return True
        else:
            return False
    def __delitem__(self,key):              # del myTree[0]
        self.delete(key)
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.getLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent = currentNode)
                currentNode.calHeight()                
                self.updataBalance_put(currentNode.leftChild)       #   新建节点，改变因子
        else:
            if currentNode.getRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent = currentNode)
                print("d",currentNode.rightChild.balanceFactor)
                currentNode.calHeight()
                self.updataBalance_put(currentNode.rightChild)
    def updataBalance_put(self,node):       #   因为插入节点，balance factory 改变
        print("before updataBalance",node.balanceFactor)
        if node.balanceFactor > 1 or node.balanceFactor < -1:       #   不平衡时候，改变树的结构
            print("D",node.balanceFactor)
            self.rebalance(node)
            return
        if node.parent != None:
            node.parent.calBalanceFactor()
            if node.parent.balanceFactor != 0 :
                self.updataBalance_put(node.parent)
    def rotateLeft(self,rotRoot):       #   左旋
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else :
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else :
                rotRoot.parent.leftChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.calBalanceFactor()
        newRoot.calBalanceFactor()
        # rotRoot.balanceFactor = rotRoot.balanceFactor + \
        #                         1 - min(newRoot.balanceFactor,0)
        # newRoot.balanceFactor = newRoot.balanceFactor + \
        #                         1 + max(rotRoot.balanceFactor,0)
    def rotateRight(self,rotRoot):      #   右旋
        newRoot = rotRoot.leftChild        
        rotRoot.leftChild = (newRoot.rightChild if newRoot else None)
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else :
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else :
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot        
        rotRoot.calBalanceFactor()        
        newRoot.calBalanceFactor()
        # rotRoot.balanceFactor = rotRoot.balanceFactor + \
        #                         1 - min(newRoot.balanceFactor,0)
        # newRoot.balanceFactor = newRoot.balanceFactor + \
        #                         1 + max(rotRoot.balanceFactor,0)
    def rebalance(self,node):       #   改变树的结构，使之重新平衡
        F = node.parent
        if node.balanceFactor < 0 :     # R 
            if node.rightChild.balanceFactor > 0:   # L
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0 :     # L 
            if node.leftChild.balanceFactor < 0:   # R
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
        unchanged = True
        while F and unchanged:
            oldH = F.height
            F.calBalanceFactor()
            unchanged = oldH==F.height
            F = F.parent
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key :
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    def delete(self,key):        
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove :
                print(nodeToRemove)
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('error,key not in tree')

        elif self.size == 1 and self.root.key == key :
            self.root = None
            self.size = 0
        else :
            raise  KeyError('error,key not in tree')    
    def remove(self,currentNode):           #   删除节点
        if currentNode.isLeaf():        #叶节点，直接删
            if currentNode.isLeftChild() :      
                currentNode.parent.leftChild = None
                currentNode.parent.balanceFactor -= 1
            else :
                currentNode.parent.rightChild = None 
                currentNode.parent.balanceFactor += 1
            if currentNode.parent:
                #currentNode.parent.calHeight()
                self.updataBalance_put(currentNode.parent)
        elif currentNode.hasBothChildren():     #   左右子树都存在
            succ = currentNode.findSuccessor()  #   找到后继节点：大于本节点的最小节点
            F = succ.parent
            succ.splitMinOut()  #   摘除节点
            #   重新赋给原来位置的节点，只需要key，value，其他位置（父子）关系不变
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            if F:
                F.calHeight()
                self.updataBalance_put(F)
        else :      #   只有一个子树存在
            if currentNode.getLeftChild():      #   有左子树
                
                if currentNode.isLeftChild():       #   自己是左子树
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                    # currentNode.parent.balanceFactor -= 1
                elif currentNode.isRightChild():    #   自己是右子树
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                    # currentNode.parent.balanceFactor += 1
                
                else:               #   自己是root
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild)
            else :      #   有右子树                
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                    # currentNode.parent.balanceFactor -= 1
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                    # currentNode.parent.balanceFactor += 1
                
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild)
            if currentNode.parent:                
                currentNode.parent.calBalanceFactor()
                self.updataBalance_put(currentNode.parent)
        self.root.calBalanceFactor()
    def out(self, start_node = None):
        if start_node == None:
            start_node = self.root
        space_symbol = "*"
        spaces_count = 100
        out_string = ""
        initial_spaces_string  = space_symbol * spaces_count + "\n" 
        if not start_node:
            return "AVLTree is empty"
        else:
            level = [start_node]
            while (len([i for i in level if (not i is None)])>0):
                level_string = initial_spaces_string
                for i in range(len(level)):
                    j = (i+1)* spaces_count // (len(level)+1)+1
                    
                    level_string = level_string[:j] + (str(level[i]) if level[i] else space_symbol) + level_string[j+1:]
                level_next = []
                for i in level:
                    level_next += ([i.leftChild, i.rightChild] if i else [None, None])
                level = level_next
                out_string += level_string                    
        return out_string
if __name__ == '__main__':
    # myTree = BinarySearchTree()
    # myTree[0] = 'red'
    # myTree.put(1,'blue')
    # myTree[3] = "3"
    # myTree[5] = [5]
    # myTree[4] = '4'
    # print(myTree.get(0))
    # print(myTree[1])
    # print(myTree.size)
    # for x in myTree:
    #     print(x,myTree[x])
    # myTree.delete(3)
    # del myTree[1]
    # for x in myTree:
    #     print(x,myTree[x])
    myTree = AVL_BinarySearchTree()
    myTree[0] = 'red'
    # print(myTree.root)
    myTree.put(1,'blue')
    # print(myTree.root)
    myTree[3] = "3"
    print("===3===")
    # print(myTree.root)
    # print(myTree.root.leftChild)
    # print(myTree.root.rightChild)
    # print(myTree.root.rightChild.rightChild)
    myTree[4] = [4]
    print("===4===")
    # print(myTree.root.key)
    # print(myTree.root.leftChild)
    # print(myTree.root.rightChild.key)
    myTree[5] = '5'
    print("===5===")
    # print(myTree.root.key)
    # print(myTree.root.leftChild.key)
    # print(myTree.root.rightChild.key)
    myTree[6] = '6'
    myTree[7] = '7'
    myTree[8] = '8'
    myTree[18] = '8'
    
    print("----9----")
    # print(myTree.root)
    # print(myTree.root.leftChild)
    # print(myTree.root.rightChild)
    # print(myTree.root.leftChild.leftChild)
    # print(myTree.root.leftChild.rightChild)
    # print(myTree.root.rightChild.leftChild)
    # print(myTree.root.rightChild.rightChild)
    print("***")
    
    myTree[10] = '8'
    print(myTree.out())
    myTree[11] = '8'
    myTree[12] = '8'
    print(myTree.out)
    myTree[13] = '8'
    print(myTree.out())
    myTree[14] = '8'
    myTree[15] = '8'
    print(myTree.out)
    '''
    myTree.delete(5)
    print("----=5-----")
    print(myTree.out())
    # print(myTree.root.key,myTree.root.balanceFactor)
    # print(myTree.root.leftChild.key,myTree.root.leftChild.balanceFactor)
    # print(myTree.root.rightChild.key,myTree.root.rightChild.balanceFactor)
    # print(myTree.root.leftChild.leftChild.key,myTree.root.leftChild.leftChild.balanceFactor)
    # print(myTree.root.leftChild.rightChild.key,myTree.root.leftChild.rightChild.balanceFactor)
    myTree.delete(18)
    print("----delete18-----")
    print(myTree.out())
    print("===")
    del myTree[1]
    print(myTree.out())
    myTree.delete(10)
    print("----delete10-----")
    print(myTree.out())
    print("===-11======")
    del myTree[11]
    print(myTree.out())
    myTree.delete(12)
    print("----delete12-----")
    print(myTree.out())
    print("===-13======")
    del myTree[13]
    print(myTree.out())
    
    myTree.delete(14)
    print("----delete14-----")
    print(myTree.out())
    print("===-15======")
    del myTree[15]
    print(myTree.out())
    '''
    for x in range(20,35):
        myTree[x] = x
        print("====={}=====".format(x))
        print(myTree.out())
    for x in range(20,35):
        del myTree[x]
        print("====={}=====".format(x))
        print(myTree.out())