import turtle

trt = turtle.Turtle()

scr = turtle.Screen()

scr.bgcolor('black')

scr.title("colored benzene design")

trt.speed(0)

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

for i in range(300):
    trt.pencolor(rainbow[i%6])
    trt.width(i/100 +1)
    trt.forward(i)
    trt.left(59)

trt.hideturtle()
turtle.done()

#lets run
