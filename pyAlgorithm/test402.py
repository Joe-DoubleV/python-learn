import turtle
convString = '0123456789ABCDEF'
def toStr(num,base):
    if num < base:
        return convString[num]
    else :
        return toStr(num//base,base)+convString[num%base]
    # print(toStr(10,2))
colormap = ['blue','red','green','yellow','orange']
t = turtle.Turtle()
def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()
def getMid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
def sierpinski(degree,points):
    pointsleft = {'left':points['left'],
                  'right':getMid(points['left'],points['right']),
                  'top':getMid(points['left'],points['top'])}
    pointstop = {'left':getMid(points['top'],points['left']),
                 'right':getMid(points['top'],points['right']),
                 'top':points['top']}
    pointsright = {'left':getMid(points['right'],points['left']),
                   'right':points['right'],
                   'top':getMid(points['top'],points['right'])}        

    drawTriangle(points,colormap[degree])
    if degree > 0:
        sierpinski(degree -1 ,pointsleft)
        sierpinski(degree -1 ,pointstop)
        sierpinski(degree -1 ,pointsright)

def drawFourangle(point,length,color):
    t.fillcolor(color)
    t.penup()
    t.goto(point)
    t.pendown()
    t.begin_fill()
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.end_fill()

def getCoordinate(p,l):
    pointslist=[]
    pointslist.append(p)
    pointslist.append((p[0]+l,p[1]))
    pointslist.append((p[0]+2*l,p[1]))

    pointslist.append((p[0],p[1]-l))
    pointslist.append((p[0]+l,p[1]-l))
    pointslist.append((p[0]+2*l,p[1]-l))

    pointslist.append((p[0],p[1]-l*2))
    pointslist.append((p[0]+l,p[1]-l*2))
    pointslist.append((p[0]+2*l,p[1]-l*2))
    return pointslist 

def four(degree,length,point):
    drawFourangle(getCoordinate(point,length/3)[4],length/3,'white')
    if degree > 0 :
        four(degree-1,length/3,getCoordinate(point,length/3)[0])
        four(degree-1,length/3,getCoordinate(point,length/3)[1])
        four(degree-1,length/3,getCoordinate(point,length/3)[2])
        four(degree-1,length/3,getCoordinate(point,length/3)[3])
        four(degree-1,length/3,getCoordinate(point,length/3)[5])
        four(degree-1,length/3,getCoordinate(point,length/3)[6])
        four(degree-1,length/3,getCoordinate(point,length/3)[7])
        four(degree-1,length/3,getCoordinate(point,length/3)[8])
def main():
    point = (-300,450)
    length = 810
    degree = 3
    drawFourangle(point,length,'blue')  
    four(degree,length,point)    

if __name__ == '__main__':
    # points = {'left':(-200,-100),
    #           'top':(0,200),
    #           'right':(200,-100)}
    # sierpinski(5,points)
    # turtle.done()       
    main()

    turtle.done()