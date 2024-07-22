import turtle


def draw_fence(x, y, kolvo, h, color):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.screen.setup(1366, 768)

    def draw_board(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("black", color)
        t.begin_fill()
        t.left(180)
        t.forward(50)
        t.right(90)
        t.forward(h)
        for i in range(2):
            t.right(60)
            t.forward(50)
        t.right(60)
        t.forward(h)
        t.right(90)
        t.forward(50)
        t.right(180)
        t.forward(50)
        t.end_fill()

    x_start = x
    y_start = y
    for _ in range(kolvo):
        draw_board(x_start, y_start)
        x_start += 87

    turtle.done()


draw_fence(-100, -300, 8, 400, 'red')