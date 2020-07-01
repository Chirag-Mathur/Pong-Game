#A simple pong game
import turtle

win = turtle.Screen()
win.title("Pong Game by mathursahab")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

#Scores
left_score =0
right_score =0

#paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("red")
paddle_left.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_left.penup()
paddle_left.goto(-350,0)

#paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("red")
paddle_right.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_right.penup()
paddle_right.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =1
ball.dy =-1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Left Player: {} Right Player: {}".format(left_score, right_score), align = "center", font=("Arial", 24, "bold"))


#Functions
def paddle_left_up():
    y = paddle_left.ycor()
    y=y+20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y=y-20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y=y+20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y=y-20
    paddle_right.sety(y)




#Keybindings
win.listen()
win.onkeypress(paddle_left_up,"w")
win.onkeypress(paddle_left_down,"s")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")


#Main game loop
while True:
    win.update()
    #BallMovements
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #GameBorders
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1;
        left_score+=1;
        pen.clear()
        pen.write("Left Player: {} Right Player: {}".format(left_score, right_score), align = "center", font=("Arial", 24, "bold"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1;
        right_score+=1;
        pen.clear()
        pen.write("Left Player: {} Right Player: {}".format(left_score, right_score), align = "center", font=("Arial", 24, "bold"))
    #BallandPaddleColliusion
    if ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<paddle_right.ycor()+60 and ball.ycor()>paddle_right.ycor()-60:
        ball.setx(340)
        ball.dx*=-1
    if ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()<paddle_left.ycor()+60 and ball.ycor()>paddle_left.ycor()-60:
        ball.setx(-340)
        ball.dx*=-1