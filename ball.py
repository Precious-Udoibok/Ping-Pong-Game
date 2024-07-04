from turtle import Turtle

#create the ball for the ping pong game
#at position (0,0) and move it to the top right of the screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_value = 0.1


    def move(self):
        '''Move the ball by changing the x and y coordinate'''
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        '''chnage the movement of the y move
        by multiplying it by -1 so that it can subtract instead of add to bounce back'''
        self.y_move *= -1

    def bounce_x(self):
        '''chnage the movement of the x move
        by multiplying it by -1 so that it can subtract instead of add to bounce back'''
        self.x_move *= -1
        self.speed_value*=0.9 #change the ball speed by multiplying it by 0.9


    def reset_position(self):
        '''reset the ball position to the middle of the screen'''
        self.speed_value = 0.1 #set the ball speed to 0.1 when the game reset
        self.goto(0,0)
        self.bounce_x()


