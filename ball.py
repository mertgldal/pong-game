from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    # Function for the ball move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Function for the collision with the top and bottom walls
    def bounce_y(self):
        self.y_move *= -1

    # Function for the collision with the paddles
    def bounce_x(self):
        self.x_move *= -1

    # Function for the reset the game
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
