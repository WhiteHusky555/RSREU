import turtle
import math
import random

win = turtle.Screen()
win.setup(800, 600)

t = turtle.Turtle()
t.speed(2)


def draw_triangle(a, b):
    t.clear()
    t.penup()
    t.goto(-0, 0)
    t.showturtle()
    t.pendown()
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.goto(0, 0)

def calculate_trigonometry(a, b):
    c = math.sqrt(a**2 + b**2)
    alpha = math.atan(b/a)
    sin_alpha = math.sin(alpha)
    cos_alpha = math.cos(alpha)
    tan_alpha = math.tan(alpha)
    cot_alpha = 1/tan_alpha
    return sin_alpha, cos_alpha, tan_alpha, cot_alpha

def print_results(sin_alpha, cos_alpha, tan_alpha, cot_alpha):
    t.hideturtle()
    t.penup()
    t.goto(-300, 100)
    t.write(f'синус={"%.3f" % sin_alpha}\nкосинус={"%.3f" % cos_alpha}\nтангенс={"%.3f" % tan_alpha}\nкотангенс={"%.3f" % cot_alpha}', font=("Arial", 18))


def generate_and_draw():
    a = random.randint(10, 100)
    b = random.randint(10, 100)
    draw_triangle(a, b)
    sin_alpha, cos_alpha, tan_alpha, cot_alpha = calculate_trigonometry(a, b)
    print_results(sin_alpha, cos_alpha, tan_alpha, cot_alpha)

button = turtle.Turtle()
button.hideturtle()
button.penup()
button.goto(-300, 200)
button.write("Click me!", font=("Arial", 24, "bold"))

def on_click(x, y):
    if (-300 <= x <= -100) and (200 <= y <= 300):
        generate_and_draw()

win.onscreenclick(on_click)

turtle.mainloop()
