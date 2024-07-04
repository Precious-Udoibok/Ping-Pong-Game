from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

#creating a screen of width 800 and height 600 and background color of black.
my_screen = Screen()
my_screen.setup(width=800,height=600)
my_screen.bgcolor('black')
my_screen.title('Pong')
#turn off the animation
my_screen.tracer(0)
my_screen.listen() #listen to the keys that will be pressed

#creating the left and right paddle
#passing in a tuple of x and y coordinate
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

#create a ball from the Ball class
my_ball = Ball()

#controlling the right paddle with the up and down arrow keys
my_screen.onkeypress(right_paddle.up,'Up')
my_screen.onkeypress(right_paddle.down,'Down')

#Create the score for right and left players
score_board = ScoreBoard()

#controlling the left paddle with the w and s keys
my_screen.onkeypress(left_paddle.up,'w')
my_screen.onkeypress(left_paddle.down,'s')

is_game_on = True
while is_game_on:
    time.sleep(my_ball.speed_value)#pause the loop for 0.1 second
    #it needs a while loop to continue updating
    #update the screen
    my_screen.update()
    my_ball.move()

    #Detect the ball Collision with the wall.
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    #Detect collision with right and left Paddles
    '''if the distance from the ball and the right and left paddles is less than 50
    and the ball x coordinate has pass -320 and -320 then its bounce back'''
    if (my_ball.distance(right_paddle) < 50 and my_ball.xcor() > 320
    or my_ball.distance(left_paddle) < 50 and my_ball.xcor() < -320):
        my_ball.bounce_x()

    #Detect when the right paddle misses the ball and move the ball in the other players direction.
    #the left player scores a point
    if my_ball.xcor() > 380 :
        my_ball.reset_position()
        score_board.l_points()

    #Detect when the left paddle misses the ball and move the ball in the other players direction.
    #right player scores a point
    if my_ball.xcor() < -380:
        my_ball.reset_position()
        score_board.r_points()




my_screen.exitonclick()
