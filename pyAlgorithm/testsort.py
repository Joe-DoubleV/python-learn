def bubbleSort(mlist):
    '''冒泡排序法'''
    print(mlist)
    l = len(mlist)
    for x in range(l-1,0,-1):
        exchange = False
        for i in range(x):
            if mlist[i] > mlist[i+1]:
                exchange = True
                mlist[i],mlist[i+1] = mlist[i+1],mlist[i]
        if not exchange:
            break
        print(mlist)
        
def selectSort(mlist):
    '''选择排序'''
    print(mlist)
    l = len(mlist)
    for x in range(l-1):
        maxIndex = 0
        for i in range(1,l-x):
            if mlist[i] > mlist[maxIndex]:
                maxIndex = i
        mlist[maxIndex],mlist[l-x-1] = mlist[l-x-1],mlist[maxIndex]
        print(mlist)

def insertSort(items):
    print(items)
    for x in range(1,len(items)):
        current = items[x]
        done = False
        for i in range(x-1,-1,-1):
            if items[i] < current:
                done = True
                items[i+2:x+1] = items[i+1:x]
                items[i+1] = current
                break
        if not done:
            items[1:x+1] =  items[0:x]
            items[0] = current            
        # print(items)
def quickSort(items):
    _quickSort(items,0,len(items)-1 )
def _quickSort(items, start, end):
    """递归调用划分和排序"""
    if start < end:
        pos = _partition(items, start, end)
        _quickSort(items, start, pos - 1)
        _quickSort(items, pos + 1, end)


def _partition(items, start, end):
    """划分"""
    pivot = items[end]
    i = start - 1 
    print(items)
    for j in range(start, end):
        if items[j] < pivot:
            i += 1
            items[i], items[j] = items[j], items[i]
        print(items,i,j)
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1

if __name__ == '__main__':
    items = [75, 37, 12, 68, 55, 87, 81, 70]
    # bubbleSort(items)
    # selectSort(items)
    
    # insertSort(items[::-1])
    # quickSort(items)
    print(_partition(items,0,7))
    # quickSort(items)
    print(items)
    # for x in range(1,1):
    #     print(x)