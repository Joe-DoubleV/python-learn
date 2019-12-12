#根据数据文件在窗口中动态路径绘制
from turtle import*
 
def main():
    #设置窗口信息
    title('数据驱动的动态路径绘制')
    setup(800, 600, 0, 0)
    #设置画笔
    # pen = turtle.Turtle()
    color("red")
    width(5)
    shape("turtle")
    speed(5)
    #读取文件
    result=[]
    file = open("file/file1.txt","r")
    for line in file:
        result.append(list(map(float, line.split(','))))
    print(result)
    #动态绘制
    for i in range(len(result)):
        color((result[i][3],result[i][4],result[i][5]))
        forward(result[i][0])
        if result[i][1]:
            rt(result[i][2])
        else:
            lt(result[i][2])
    goto(0,0)
    done()
 
 
if __name__ == '__main__':
    main()