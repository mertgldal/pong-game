import time
from turtle import Screen

from Scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

# screen creation
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title(titlestring="Pong")
screen.tracer(0)

# paddle object creation and their starting locations
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

x_score = Scoreboard((100, 240))
y_score = Scoreboard((-100, 240))

# ball object creation
ball = Ball()


# Paddles control
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
game_speed = 0.1

while game_is_on:
    # To see the ball on the screen, put the program to sleep for 0.1 seconds,
    # otherwise it will move too fast to be seen.
    time.sleep(game_speed)

    screen.update()
    ball.move()

    # detect collision with the top and the bottom of the screen
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        game_speed /= 1.2

    # if R paddle misses
    if ball.xcor() > 380:
        y_score.update_score()
        game_speed = 0.1
        ball.reset()

    # if l paddle misses
    if ball.xcor() < -380:
        x_score.update_score()
        game_speed = 0.1
        ball.reset()

screen.exitonclick()
