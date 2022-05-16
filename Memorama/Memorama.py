from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😇', '😉', '😊', '🙂', '🙃', '☺', '😋', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '🥲', '🤪', '😜', '😝', '😛', '🤑', '😎', '🤓', '🥸', '🧐'] * 2
#tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
contador = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global contador
    contador += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    up()
    goto(-290,-290)
    write("Numero de taps: " + str(contador), font=('Arial', 20, 'normal'), align='left')
    goto(290,-245)
    if (not any(hide)):
        write("Ganaste un auto!!, Felicidades", font=('Arial', 20, 'normal'), align='right')
        
    ontimer(draw, 100)


writer = Turtle()
tracer(False)


def info_alumnos():
    writer.hideturtle()
    writer.up()
    writer.goto(0,250)
    writer.color('blue')
    writer.write("Kevin ALberto Crisostomo A00832188", align='center',font=('chalkboard',15,'normal'))
    writer.goto(0,230)
    writer.color('pink')
    writer.write("Alejandro Melendez Torres A00832494", align='center',font=('chalkboard',15,'normal'))
    writer.goto(0,210)
    writer.color('green')
    writer.write("José Edmundo Romo Castillo A01197772", align='center',font=('chalkboard',15,'normal'))

#shuffle(tiles)
setup(600, 600, 370, 0)
info_alumnos()
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
