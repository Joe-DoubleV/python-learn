from basic.Queue import Queue
import random

class Printer():
    def __init__(self,ppm):
       self.pagerate = ppm
       self.currentTask = None
       self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        return self.currentTask != None

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

class Task():
    """docstring for Task"""
    def __init__(self, time):
        self.timetamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timetamp

    def getPages(self):
        return self.pages
    
    def waitTime(self,currenttime):
        return currenttime - self.timetamp
def newPrintTask():
    ran = random.randrange(1,181)

    if ran ==10:
        return True
    else:
        return False

def simulation(numSeconds,pagesPerMinute):
    lapprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not lapprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            lapprinter.startNext(nexttask)
        lapprinter.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f seconds %3d tasks remaining."%(averageWait,printQueue.size()))
# for x in range(10):
#     simulation(3600,10)
    '''
Average Wait 124.67 seconds   0 tasks remaining.
Average Wait 209.38 seconds   0 tasks remaining.
Average Wait  98.81 seconds   0 tasks remaining.
Average Wait  71.59 seconds   7 tasks remaining.
Average Wait 318.25 seconds   3 tasks remaining.
Average Wait 336.59 seconds   1 tasks remaining.
Average Wait 160.75 seconds   1 tasks remaining.
Average Wait 165.80 seconds   1 tasks remaining.
Average Wait  70.21 seconds   4 tasks remaining.
Average Wait 177.79 seconds   2 tasks remaining.
    '''
strings = "qwerty"
alist = strings[:]
print(alist)