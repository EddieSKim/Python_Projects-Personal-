# Creating a simple pong game
# Python version 3.8.5

import turtle
import winsound

win = turtle.Screen()
win.title("Simple Pong Game")
win.bgcolor("black")  # try to animate this
win.setup(width=800, height=600)
win.tracer(0)   # Manually refresh the window

# Score
score_a = 0
score_b = 0

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)  # speed of animation : maximum speed
pad_a.shape("square")
# width is y direction, length is x direction
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.color("white")
pad_a.penup()   # no drawing a line when moving
pad_a.goto(-350, 0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)  # speesd of animation : maximum speed
pad_b.shape("square")
# width is y direction, length is x direction
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.color("white")
pad_b.penup()   # no drawing a line when moving
pad_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # move by 0.2 pixels
ball.dy = 0.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()    # hiding the object, only need to see the text it writes
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "bold"))

# Movement Functions

# paddle a movement


def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)


def pad_a_dw():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

# paddle b movement


def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)


def pad_b_dw():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)


# Keyboard binding
win.listen()    # action listener
win.onkeypress(pad_a_up, "w")
win.onkeypress(pad_a_dw, "s")
win.onkeypress(pad_b_up, "Up")  # 'Up' is the arrow key
win.onkeypress(pad_b_dw, "Down")


# main loop
while True:
    win.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if pad_a.ycor() > 250:
        pad_a.sety(250)

    if pad_b.ycor() > 250:
        pad_b.sety(250)

    if pad_a.ycor() < -240:
        pad_a.sety(-240)

    if pad_b.ycor() < -240:
        pad_b.sety(-240)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # SND_ASYNC will play sound in the background, must be in specific format
        winsound.PlaySound(
            'bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # SND_ASYNC will play sound in the background
        winsound.PlaySound(
            'bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "bold"))

    if ball.xcor() < -388:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "bold"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(
            'bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(
            'bounce.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
