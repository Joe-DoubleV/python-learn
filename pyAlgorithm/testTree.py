from basic.BinaryTree import BinaryTree
from basic.stack import Stack
import operator
# from basic.BinarySearchTree import AVL_BinarySearchTree
import basic.BinarySearchTree as bst
import urllib.request
def preorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getRootVal())
        
        preorder(tree.getRightChild())
opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
def evlauate(parseTree):        #后序遍历
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC :
        fn = opers[parseTree.getRootVal()]
        return fn(evlauate(leftC),evlauate(rightC))
    else:
        # print(parseTree.getRootVal())
        return parseTree.getRootVal()

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree("")
    pStack.push(eTree)  
    currentTree = eTree                                 #入栈下降
    for i in fplist:
        if i =='(':
            currentTree.insertLeft("")
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()    #入栈下降
        elif i not in ['+','-','*','/',')'] :
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent                        #出栈上升                   
        elif i in ['+','-','*','/'] :
            currentTree.setRootVal(i)
            currentTree.insertRight("")
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()   #入栈下降
        elif i ==')':
            currentTree = pStack.pop()                  #出栈上升
        else:
            raise ValueError
    return eTree
if __name__ == '__main__':
    
    # r = BinaryTree('a')
    # r.insertLeft('b')
    # r.insertRight('c')
    # r.getLeftChild().insertLeft('d')
    # r.getLeftChild().insertRight("e")
    # preorder(r)
    # print()
    # r.preorder()
    # print()
    # r.midorder()
    # print()
    # r.aforder()

    # fpexp = "( 3 * ( 2 + 4 ) )"
    # eTree = buildParseTree(fpexp)
    # # print(eTree)
    # preorder(eTree)
    # print(evlauate(eTree))
    # 
    myTree = bst.AVL_BinarySearchTree()
    myTree[0] = 'red'
    print(myTree.root.key)
    myTree.put(1,'blue')
    print(myTree.root.key)
    myTree[3] = "3"
    print(myTree.root.key)
    myTree[4] = [4]
    print(myTree.root.key)
    myTree[5] = '5'
    print(myTree.root.key)
    myTree[6] = '6'
    print(myTree.root.key)
    # response = urllib.request.urlopen("https://www.yinlingw.com/caijing/41316.html")
    # #urlopen("https://www.yinlingw.com/caijing/41316.html")
    # print(response.read().decode())
    n = 10
    s = 0
    for k in range(1, n-1):
        for j in range(n, k-1, -1):
            s += 1
    print(s)

    Header = {"a":"b"+"c\\\\Ass"}
    print(Header)
