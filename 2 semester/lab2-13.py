import turtle


def draw_fence():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()


    def draw_board(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("black", "orange")
        t.begin_fill()
        t.left(180)
        t.forward(50)
        t.right(90)
        t.forward(150)
        for i in range(2):
            t.right(60)
            t.forward(50)
        t.right(60)
        t.forward(150)
        t.right(90)
        t.forward(50)
        t.right(180)
        t.forward(50)
        t.end_fill()

    x_start = -150
    y = 0
    for _ in range(6):
        draw_board(x_start, y)
        x_start += 87

    turtle.done()


draw_fence()