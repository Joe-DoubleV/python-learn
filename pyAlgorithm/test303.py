from basic.stack import Stack
from basic.Queue import Queue

def parChecker(sybomlString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(sybomlString) and balanced:
        symbol = sybomlString[index]
        if symbol == '(':
            s.push(symbol)
        elif s.isEmpty():
            balanced = False
        else:
            s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False
def matches(open,close):
    opens = "{[("
    closes = "}])"
    return opens.index(open) == closes.index(close)

def parCheckers(sybomlString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(sybomlString) and balanced:
        symbol = sybomlString[index]
        if symbol in '([{':
            s.push(symbol)
        elif s.isEmpty():
            balanced = False
        else:
            top = s.pop()
            if not matches(top, symbol) :
                return False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def divideBy2(decNumber):
    remStack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber = decNumber//2
    binString = ""
    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())
    return binString

def divideByN(decNumber,N = 2):
    digits = "0123456789ABCD"
    remStack = Stack()
    while decNumber > 0:
        rem = decNumber % N
        remStack.push(digits[rem])
        decNumber = decNumber//N
    binString = ""
    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())
    return binString

def infixToPostfit(infiexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfitList = []
    tokenList = infiexpr.split()
    print(tokenList)
    for token in tokenList:
        if token in "ABCDEFG" or token in "0123456789":
            postfitList.append(token)
        elif token =='(':
            opStack.push(token)
        elif token ==')':
            topToken = opStack.pop()
            while topToken !='(':
                postfitList.append(topToken)
                topToken = opStack.pop()
        else :
            while (not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]):
                postfitList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfitList.append(opStack.pop())
    return " ".join(postfitList)


print(parChecker("((())))"))
print(parChecker("(())((()))()(())"))
print(parCheckers("((){}{}[])"))
print(parCheckers("{[()]}"))
print(divideByN(42))

# print(infixToPostfit("A + B * C - D "))
s = "asdf"
alist = s[:]
print(alist)