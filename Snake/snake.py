from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
speed = vector (10,10)


def change(x, y):
    "hange snake direction."
    aim.x = x
    aim.y = y

def faster():
    speed.x=speed.x+5
    speed.y=speed.y+5

def slower():
    speed.x=speed.x-5
    speed.y=speed.y-5

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: faster(),'+')
onkey(lambda: slower(),'-')
onkey(lambda: change(speed.x, 0), 'Right')
onkey(lambda: change(-speed.x, 0), 'Left')
onkey(lambda: change(0, speed.y), 'Up')
onkey(lambda: change(0, -speed.y), 'Down')
move()
done()
