from turtle import Turtle,Screen

def etch_a_sketch():
    t = Turtle()
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.colormode(255)

    def move_forward():
        t.forward(10)

    def move_backward():
        t.backward(10)

    def turn_right():
        t.right(10)

    def turn_left():
        t.left(10)

    screen.listen()
    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(screen.resetscreen, "c")
    screen.onkey(t.penup, "q")
    screen.onkey(t.pendown, "e")
    screen.exitonclick()

etch_a_sketch()