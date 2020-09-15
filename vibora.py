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
    
    #Se define una variable booleana para controlar que la comida no tope con los límites
    limite = True
    #Para cada paso que dé la serpiente, la comida se moverá un paso
    if head != food:
        #El ciclo while se ejecutará hasta que se genere una posición que no tope con el límite correspondiente
        while limite == True: 
            #Se genera un número random para representar la dirección a la que se moverá la comida
            direccion = randrange(1,5) #1 arriba, 2 derecha, 3 izquierda, 4 abajo
            #Dependiendo de la dirección la coordenada correspondiente de la comida se moverá (10 posiciones para que la serpiente pueda coincidir) 
            if direccion == 1 and food.y < 190:
                food.y += 10
                limite = False
            elif direccion == 2 and food.x < 190:
                food.x += 10
                limite = False
            elif direccion == 3 and food.x > -200:
                food.x -= 10
                limite = False
            elif direccion == 4 and food.y > -200:
                food.y -= 10
                limite = False
            
    snake.append(head)

    if head == food: 
        print('Snake:', len(snake)) #Imprime la longitud de la serpiente
        #Si la cabeza llega a la posición de la comida, la comida se cambia de lugar
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