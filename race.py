# Turtle Race

from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
screen.setup(width=500,height=400)

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
y = [100, 60, 20, -20, -60, -100]
turtles = []

is_race_on = False
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
print(f"User's bet: {user_bet}")

for i in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.teleport(x=-230,y=y[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            print(f"The winner is: {turtle.pencolor()}")
            winner = turtle.pencolor()
            is_race_on = False
            if user_bet == winner:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")

        turtle.penup()
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()