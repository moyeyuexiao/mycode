import turtle
import turtle as T
import random

def draw_tree(distance,t):
    if distance>5:
        t.pensize(3)
        t.color('peru')
        t.forward(distance*2)
        t.right(20)
        draw_tree(distance/1.6, t)
        t.left(40)
        draw_tree(distance / 1.6, t)
        if distance<7:
            t.color('pink')
            t.pensize(5)
            t.color('azure')
            t.right(20)
            t.backward(distance * 2)
        else:
            t.color('peru')
            t.right(20)
            t.backward(distance*2)

def fun(t):
    for i in range(50):
        t.up()
        x = random.randint(50,300)
        y = random.randint(50,300)
        t.color('grey')
        t.setx(x)
        t.sety(y)
        t.color('pink')
        t.down()
        t.circle(2)

if __name__ == '__main__':
    t = T.Turtle()
    turtle.bgcolor('black')
    t.left(90)
    t.speed(0.001)
    t.up()
    t.backward(200)
    t.down()
    t.color('brown')
    t.pensize(3)
    draw_tree(60,t)
    fun(t)