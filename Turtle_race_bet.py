from turtle import Turtle,Screen
from random import randint

def turtle_race():
    screen = Screen()
    user_bet = screen.textinput(title="Make Your Bet!", prompt="Which Turtle will win the race? Enter a color: ")
    screen.setup(width=500, height=400)
    screen.colormode(255)

    t1 = Turtle()
    t1.shape("turtle")
    t1.color("red")
    t1.penup()
    t1.goto(-230,50)

    t2 = Turtle()
    t2.shape("turtle")
    t2.color("orange")
    t2.penup()
    t2.goto(-230,25)

    t3 = Turtle()
    t3.shape("turtle")
    t3.color("blue")
    t3.penup()
    t3.goto(-230,0)

    t4 = Turtle()
    t4.shape("turtle")
    t4.color("purple")
    t4.penup()
    t4.goto(-230,-25)

    t5 = Turtle()
    t5.shape("turtle")
    t5.color("green")
    t5.penup()
    t5.goto(-230,-50)

    colors = ["purple","red", "blue", "green", "orange"]
    turtles = [t1,t2,t3,t4,t5]

    for turtle in turtles:
        turtle.speed(0)

    race_on = False

    if user_bet.lower() in colors:
        race_on = True
    else:
        print(f"Wrong color input")
        screen.clear()
        turtle_race()

    while race_on:
        for turtle in turtles:
            turtle.forward(randint(1,10))

        for turtle in turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                race_on = False
                if user_bet.lower() == winning_color:
                    print(f"\nYou win. The winning turtle was {winning_color}!")
                else:
                    print(f"\nYou Lose. The winning turtle was {winning_color}!")

    screen.exitonclick()

turtle_race()