"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

#Se crean vectores para las posiciones de los elementos del juego
food = vector(0, 0) 
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction." #Cambia las coordenadas x y y de la dirección
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries." #Verifica que la serpiente no haya topado con el límite
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment." #Dependiendo de la dirección se mueve la serpiente
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake: #Si topa con el límite o con ella mísma, la cabeza de la serpiente se hace roja
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food: #Si la cabeza llega a la posición de la comida, la comida se cambia de lugar
        print('Snake:', len(snake)) 
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake: #Color de la serpiente
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green') #Color de la comida
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0) #límites del juego
hideturtle()
tracer(False)
listen()
#Comandos para mover la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()