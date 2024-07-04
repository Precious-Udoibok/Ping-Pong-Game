from turtle import Turtle

'''Create a class call score board that will keep track of the 
right and left players scores.
'''

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self. penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        '''write the current players scores'''
        self.clear()
        self.goto(-100,200)
        self.write(arg=self.l_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(100, 200)
        self.write(arg=self.r_score, align='center', font=('Courier', 50, 'normal'))

    def l_points(self):
        '''Increment the left player score by 1 and write it on the screen'''
        self.l_score+=1
        self.update()

    def r_points(self):
        '''Increment the right player score by 1 and write it on the screen'''
        self.r_score+=1
        self.update()