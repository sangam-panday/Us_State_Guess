from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
x_pos = int(350)
y_pos = int(0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

b = Ball()
rp = Paddle((-350, 0))
lp = Paddle((350, 0))

screen.listen()
screen.onkey(rp.go_up, "Up")
screen.onkey(rp.go_down, "Down")
screen.onkey(lp.go_up, "w")
screen.onkey(lp.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    b.move()
    if b.ycor()>290 or b.ycor()<-290:
        b.bounce()
    
    if b.distance(rp) < 50 and b.xcor() > 340:
        print("Made contanct. ")

screen.exitonclick()