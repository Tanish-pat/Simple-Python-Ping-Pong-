import time
import turtle
wn=turtle.Screen()
wn.title("Pong by Me!!")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) # allows us to manually update the undow , speeds up the game

#Score
score_a=0
score_b=0

# paddle A
paddle_a=turtle.Turtle() #small t for import turtle and big T for the class Turtle. It is an object
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup() #if we don't do penup, we leave a line
paddle_a.goto(-350,0)

# paddle B
paddle_b=turtle.Turtle() 
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball=turtle.Turtle() 
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2 # dx is change in x coordinates
ball.dy=2 # since it is positive , it goes 2 up and 2 right , for now

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center",font=("Courier",24,"normal"))

#Functions
def paddle_a_up():
    y=paddle_a.ycor() #gets the turtle object's  y coordinate 
    y+=40
    paddle_a.sety(y) #sets the turtle object's  y coordinate 
    
def paddle_a_down():
    y=paddle_a.ycor()
    y-=40
    paddle_a.sety(y)
        
def paddle_b_up():
    y=paddle_b.ycor()
    y+=40
    paddle_b.sety(y)
 
def paddle_b_down():
    y=paddle_b.ycor()
    y-=40
    paddle_b.sety(y)

wn.listen()

wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



#Main game loop
while True:
    wn.update()
    
    if score_a >= 10 or score_b >= 10:
        winner = "Player A" if score_a >= 10 else "Player B"
        message = "{} wins!".format(winner)
        pen.clear()  
        pen.goto(0, 0)
        pen.write(message, align="center", font=("Courier", 36, "bold"))
        time.sleep(3)  
        pen.clear()
        wn.bye()
        
    ball.setx(ball.xcor()+ball.dx/20)
    ball.sety(ball.ycor()+ball.dy/20)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))
    
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)
        
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
