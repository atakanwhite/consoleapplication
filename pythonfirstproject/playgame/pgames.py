def pgmenu() :
    print("╔═════════════════╔═════════════════════╗═════════════════╗")
    print("║═════════════════╚═════FAMOUS BOOKS════╝═════════════════║")
    print("║         1-  Book1                                       ║ ")
    print("║         2-  Book2                                       ║ ")
    print("║         3-  Book3                                       ║ ")                            
    print("║         4-  Book4                                       ║ ")
    print("║         5-  Book5                                       ║ ")
    print("║                                                         ║ ")
    print("╚═════════════════════════════════════════════════════════╝ ")

    print(" What's your choice? ")

    choice = input()

if choice == "1" :
        from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

canvas_width = 800
canvas_height = 400

root = Tk()
root.title("Egg Catcher")
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")
c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty = 0.95
catcher_color = "blue"
catcher_width = 100
catcher_height = 100
catcher_startx = canvas_width / 2 - catcher_width / 2
catcher_starty = canvas_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height

catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3)
game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)


score = 0
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))

lives_remaining = 3
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))

eggs = []

def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)

def move_eggs():
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        c.move(egg, 0, 10)
        if eggy2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
        root.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def check_catch():
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)

def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty)
    egg_interval = int(egg_interval * difficulty)
    c.itemconfigure(score_text, text="Score: "+ str(score))

def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)

c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.focus_set()
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()

    
if choice == "2" :
      from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()
    
if choice == "3" :
        import turtle
import winsound


window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)    # stops the window from updating

#   1st Paddle
paddle_one = turtle.Turtle()
paddle_one.speed(0)     # speed of animation, '0' for MAX
paddle_one.color("white")
paddle_one.shape("square")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)  # 20*5 height
paddle_one.penup()
paddle_one.goto(-350, 0)    # (0, 0) is in middle
wid_one = 5

#   2nd Paddle
paddle_two = turtle.Turtle()
paddle_two.speed(0)     # speed of animation, '0' for MAX
paddle_two.color("white")
paddle_two.shape("square")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)    # (0, 0) is in middle
wid_two = 5

#   Ball
ball = turtle.Turtle()
ball.speed(0)     # speed of animation, '0' for MAX
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)    # (0, 0) is in middle
ball.dx = 0.2     # ball moves by 2 pixels
ball.dy = -0.2


# for scoring

score_one = 0
score_two = 0

write_score = turtle.Turtle()
write_score.speed(0)
write_score.color("white")
write_score.penup()
write_score.hideturtle()
write_score.goto(0, 260)
write_score.write("Player One: 0        Player Two: 0", align="center", font=("Courier", 24, "normal"))


# movement of paddle
def paddle_one_up():
    y = paddle_one.ycor()   # coordinates
    y += 50
    paddle_one.sety(y)


def paddle_one_down():
    y = paddle_one.ycor()   # coordinates
    y -= 50
    paddle_one.sety(y)


def paddle_two_up():
    y = paddle_two.ycor()   # coordinates
    y += 50
    paddle_two.sety(y)


def paddle_two_down():
    y = paddle_two.ycor()   # coordinates
    y -= 50
    paddle_two.sety(y)


# Keyboard Events
window.listen()
# Left one
window.onkeypress(paddle_one_up, 'w')
window.onkeypress(paddle_one_down, 's')
# right one
window.onkeypress(paddle_two_up, 'Up')
window.onkeypress(paddle_two_down, 'Down')

# main loop for the game to run
while True:
    window.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball's Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   # reversing direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   # reversing direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:   # past the paddle
        ball.goto(0, 0)
        ball.dx = -0.2
        if ball.dy > 0 : 
            ball.dy = 0.2
        else :
            ball.dy = -0.2
        score_one += 1
        write_score.clear()
        write_score.write("Player One: {}           Player Two: {}".format(score_one, score_two), align="center",
                          font=("Courier", 24, "normal"))
        
        if (wid_one != 1 and wid_two != 1) :
            wid_one -= 1
            wid_two += 1
            paddle_one.shapesize(stretch_wid=wid_one, stretch_len=1)
            paddle_two.shapesize(stretch_wid=wid_two, stretch_len=1)

    if ball.xcor() < -390:   # past the paddle
        ball.goto(0, 0)
        ball.dx = 0.2
        if ball.dy > 0 : 
            ball.dy = 0.2
        else :
            ball.dy = -0.2
        score_two += 1
        write_score.clear()
        write_score.write("Player One: {}           Player Two: {}".format(score_one, score_two), align="center",
                          font=("Courier", 24, "normal"))
        if (wid_one != 1 and wid_two != 1) :
            wid_two -= 1
            wid_one += 1
            paddle_two.shapesize(stretch_wid=wid_two, stretch_len=1)
            paddle_one.shapesize(stretch_wid=wid_one, stretch_len=1)

    # Collisions b/w ball & paddle

    if (340 < ball.xcor() < 350) and (paddle_two.ycor() + 40 > ball.ycor() > paddle_two.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.05
        ball.dy *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (-340 > ball.xcor() > -350) and (paddle_one.ycor() + 40 > ball.ycor() > paddle_one.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.05
        ball.dy *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
         
    if choice == "4" :
        
    
    if choice == "5" :
         
  
elif anamenu()
    
