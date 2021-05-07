import turtle 
import winsound

#Window----------------------------------------------------
wn = turtle.Screen() #Create Window from turtle module
wn.title("Pong Game") #Set up title name
wn.bgcolor("black") #Set up window background color
wn.setup(width=800, height=600) #Set up window size
wn.tracer(0) #Stop window from updating

# Score ---------------------------------------------------#
score_a = 0
score_b = 0

#Paddle A-------------------------------------------------
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B-------------------------------------------------
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Control functions-----------------------------------------------------------

def paddleA_up():      #Defining function to move paddle A
    y = paddleA.ycor() #Get paddleA coordinates
    y += 20            #Increment the Y position of paddle A
    paddleA.sety(y)    #Setting paddleA's current position to variable y

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

#Keyboard binding-----------------------------------------
wn.listen() #Tell the window to listen for event/keyboar input
wn.onkeypress(paddleA_up, "w") #When user presses W move paddle up
wn.onkeypress(paddleA_down, "s") #Calling function, moving paddleA down
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")



# Main game loop ----------------------------------------
while True:
    wn.update()

    #Move ball--------------------------------------------
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Walls Collision Setting----------------------------------------
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball colisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1  

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


