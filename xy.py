import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
my_pen =  turtle.Turtle()
size=0
while True:
    for i in range(4):
     my_pen.forward(size+1)
     my_pen.left(90)
     size=size-5
    size+=1


    