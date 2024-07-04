from turtle import Turtle
#Create a paddle on the right side
#with a width of 20, height of 100
#move the paddle using the up and down arrow keys
#have an x pos of 350 and y position of 0

class Paddle(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.shape('square')
        self.coordinate = coordinate
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(self.coordinate)

#create functions to move the paddle up and down
    def up(self):
        '''tell the paddle to go to it current x position and y position plus 20'''
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def down(self):
        '''move the paddle down by chaging the current y coordinate'''
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
