import turtle as T
import random
import time
def tree(self,branch):
    time.sleep(0.0005)
    if branch>3:
        if 4<=branch<=12:
            T.color('pink')
            T.pensize(random.randint(2,4))
            a=random.random()*2
            T.circle(a)
        elif 3<=branch<=4:
            T.color('white')
            T.pensize(random.randint(2,4))
            b=random.random()*2
            T.circle(b)
        else:
            T.color('sienna')
            T.pensize(branch/10)
        T.color('sienna')
        T.pensize(branch/10)
        T.forward(branch)
        a=1.5*random.random()
        T.right(20*a)
        b=1.5*random.random()
        tree(self,branch-10*b)
        T.left(40*a)
        tree(self, branch - 10 * b)
        T.right(20*a)
        T.up()
        T.backward(branch)
        T.down()

def petal(T):
    for i in range(50):
        T.up()
        T.backward(700)
        x=random.randint(-200,200)
        y=random.randint(-150,150)
        T.color('pink')
        T.setx(x)
        T.sety(y)
        T.down()
        T.circle(1)

if __name__ == '__main__':
    T.bgcolor('black')
    T.hideturtle()
    T.getscreen().tracer(10,0)
    T.left(90)
    T.backward(150)
    tree(T,60)
    petal(T)
    time.sleep(400)