import turtle as T
import time
def smileface(T):
    T.left(90)
    T.up()
    T.down()
    T.pensize(4)
    T.color('lemonchiffon')
    T.circle(120)
    T.up()
    T.forward(40)
    T.left(90)
    T.forward(80)
    T.down()
    T.color('dodgerblue')
    T.circle(5)
    T.up()
    T.forward(80)
    T.down()
    T.circle(5)
    T.up()
    T.backward(40)
    T.left(90)
    T.forward(80)
    T.down()
    T.color('lightpink')
    T.left(90)
    T.backward(30)
    T.forward(60)
    T.left(60)
    T.forward(20)
    T.left(60)
    T.right(120)
    T.backward(80)
    T.right(60)
    T.forward(20)
if __name__ == '__main__':
    T.bgcolor('deepskyblue')
    smileface(T)
    time.sleep(200)


