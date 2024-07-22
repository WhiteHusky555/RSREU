import turtle
import math
import time

# Constants
GRAVITY = 9.81
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CANNON_WIDTH = 50
CANNON_HEIGHT = 20
TARGET_WIDTH = 50
TARGET_HEIGHT = 50
PROJECTILE_RADIUS = 5
angle = 45
mass = 10
tilt = 0
gravity = 9.81

# Create screen
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

def create_shape(shape, color, width, height, x, y):
    new_shape = turtle.Turtle()
    new_shape.shape(shape)
    new_shape.color(color)
    new_shape.shapesize(width / 20, height / 20)
    new_shape.penup()
    new_shape.goto(x, y)
    return new_shape


cannon = create_shape("square", "black", CANNON_WIDTH, CANNON_HEIGHT, -400, 0)

target = create_shape("circle", "red", TARGET_WIDTH, TARGET_HEIGHT, 400, 0)
def fon():
    grass=turtle.Turtle()
    grass.hideturtle()
    grass.penup()
    grass.goto(-SCREEN_WIDTH/2, 0-30)
    grass.begin_fill()
    grass.fillcolor('green')
    grass.goto(SCREEN_WIDTH/2, 0-30)
    grass.goto(SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    grass.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
    grass.goto(-SCREEN_WIDTH/2, 0)
    grass.end_fill()
fon()
button_positions = [50, 100, 150, 200, 250]
buttons = []

for pos in button_positions:
    new_button = create_shape("square", "gray", 20, 20, -SCREEN_WIDTH / 2 + pos, -SCREEN_HEIGHT / 2 + 50)
    buttons+=[new_button]

angle = 90
mass = 10
velocity = 50

def change_angle(angle_change):
    global angle
    angle += angle_change
    cannon.right(angle_change)
    print(f'угол наведения = {angle}')

def change_mass(mass_change):
    global mass
    if mass+mass_change<1:
        print('Невозможно уменьшить вес снаряда')
    else:
        mass += mass_change
    print(f'масса = {mass}')

def shoot():
    global angle, mass, tilt
    velocity = 50
    theta = math.radians(angle)
    phi = math.radians(tilt)
    vx = -velocity * math.cos(theta) * math.cos(phi) / (mass*0.1)
    vy = velocity * math.sin(theta) * math.cos(phi) / (mass*0.1)
    x, y= -400, 0
    projectile = turtle.Turtle()
    projectile.hideturtle()
    projectile.speed(0)
    projectile.penup()
    projectile.goto(x, y)
    projectile.pendown()
    projectile.color("blue")
    hit = False
    while y >= -40:
        x += vx
        y += vy
        vy -= gravity
        projectile.goto(x, y)
        distance = math.sqrt((x - 400) ** 2 + y ** 2)
        if distance <= 50:
            hit = True
            break
    if hit:
        print('Попадание')
    else:
        print('Промах')
    time.sleep(1)
    projectile.clear()

buttons[0].onclick(lambda x, y: change_angle(-5))
buttons[1].onclick(lambda x, y: change_angle(5))
buttons[2].onclick(lambda x, y: change_mass(1))
buttons[3].onclick(lambda x, y: change_mass(-1))
buttons[4].onclick(lambda x, y: shoot())

turtle.done()
