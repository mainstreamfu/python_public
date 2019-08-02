'''
import turtle
# 这是一朵花的程序

t=turtle.Pen()
for x in range(360):
    t.forward(x)
    t.right(49)
'''
'''
# 奥运五环
'''
import turtle
turtle.width(10)#笔粗10px

turtle.color("blue")#笔颜色的
turtle.circle(50)#画圆50半径
turtle.penup()#抬笔
turtle.goto(120,0)#修改起笔点坐标
turtle.pendown()#落笔

turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(240,0)
turtle.pendown()

turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(60,-50)
turtle.pendown()

turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(180,-50)
turtle.pendown()

turtle.color("green")
turtle.circle(50)
turtle.Pen()
