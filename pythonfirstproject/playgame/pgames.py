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
        import linecache
        import random
        import time

        # colors for console
        red = "\u001B[31m"
        yellow = '\u001B[33m'
        green = '\u001B[32m'
        white = '\u001B[39m'
        blue = '\u001B[24m'


        # resets vars for new round
        def reset():
            global word, used, correct, fullWord, attempts, condition, againTimes
            word = ''
            used = []
            correct = 0
            fullWord = []
            attempts = 12
            condition = 0
            againTimes = 0


        # start function
        def start():
            global mode
            print('---< commands >---')
            print('enter any letter as your guess')
            print('enter !guess to guess the whole word')
            print('enter !used to see used letters')
            print('enter !save to save your stats')
            print('enter !end to give and end the game')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            reset()
            time.sleep(1)
            print(green + '!normal is for normal mode | lives: 12, word length any, guess wrong: -2 lives')
            print(red + '!hard is for hard mode | lives: 6, word length > 6, guess wrong: death' + white)
            mode = input('enter !normal or !hard: ')
            main()


        def again():
            global mode, attempts, endCondition, autoSave, againTimes
            if againTimes == 0:
                print('enter !save to save your results')
            print('enter !play to play again\nenter !stop to stop')
            option = input('\nenter you choice: ')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            if option == '!stop':
                exit()
            elif option == '!save':
                file = open('history', 'a')
                file.write('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
                file.write(f'{endCondition}\n')
                file.write(
                    f'word: {word[:-1]}\nmode: {mode[1:]}\nlives left: {lives}\nwrong letters: {attempts - lives}\nused letters: {len(used)}\n')
                file.write(f'used letter list: {used}\n')
                againTimes += 1
                again()
            elif option == '!play':
                reset()
                time.sleep(1)
                print(green + '!normal is for normal mode | lives: 12, word length any, guess wrong: -2 lives')
                print(red + '!hard is for hard mode | lives: 6, word length > 6, guess wrong: death' + white)
                mode = input('enter !normal or !hard: ')
                againTimes = 0
                main()
            else:
                exit()


        # stats for end of game
        def stats():
            global mode, attempts, lives, endCondition
            if attempts < 0:
                attempts = 0
            lives = attempts
            if mode == '!hard':
                attempts = 6
            else:
                attempts = 12
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            # sets end condition of the game
            if condition == 0:
                endCondition = green + 'you won' + white
            elif condition == 1:
                endCondition = red + 'you lost | you ran out of lives' + white
            elif condition == 2:
                endCondition = red + 'you lost | you guessed the wrong word' + white
            elif condition == 3:
                endCondition = red + 'you lost | you gave up' + white
            else:
                endCondition = yellow + 'you lost | no lose information' + white
            print(endCondition)
            print(
                f'word: {word[:-1]}\nmode: {mode[1:]}\nlives left: {lives}\nwrong letters: {attempts - lives}\nused letters: {len(used)}')
            print(f'used letter list: {used}')
            time.sleep(1)
            print(blue + '\ncheck out my github: https://github.com/cqb13' + white)
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            again()


        def main():
            global fullWord, word, correct, attempts, condition
            word = linecache.getline('words', random.randrange(0, 8747))
            if mode == '!hard':
                print(red + 'you are on hard mode' + white)
                attempts = 6
                while len(word) <= 6:
                    word = linecache.getline('words', random.randrange(0, 8747))
            else:
                print(green + 'you are on normal mode' + white)
            wordlength = len(word)
            # creates the word visual
            while wordlength != 0:
                fullWord.append('_')
                wordlength -= 1
            fullWord.pop()
            print(fullWord)
            # takes enter key value from words file needs it removed
            print(f'word length: {len(word) - 1}')
            print(f'lives: ' + green + f'{attempts}' + white)

            # game loop
            while attempts > 0:
                option = input('enter a guess: ')

                if option == '!used':
                    print(f'used letters: {used}')
                elif option == '!save':
                    print(yellow + 'you can do that at the end of a round' + white)
                elif option == '!end':
                    print(yellow + 'are you sure you want to give up?')
                    print('enter y to give up\nenter any key to skip' + white)
                    option = input('enter your choice: ')
                    if option == 'y':
                        condition = 3
                        stats()
                    else:
                        print('skipped')
                # option to guess the full word
                elif option == '!guess':
                    if mode == '!hard':
                        print(yellow + 'if incorrect you will lose' + white)
                    else:
                        print(yellow + 'if incorrect you will lose 2 lives')
                    print('enter y to give up\n enter any key to skip' + white)
                    option = input('enter your choice: ')
                    word = word[:-1]
                    # confirm option
                    if option == 'y':
                        option = input('enter word: ')
                        # checks if the word is right after guessing full word
                        if option == word:
                            condition = 0
                            stats()
                        # checks if you are on normal mode
                        elif option != word and mode != '!hard':
                            print(red + 'that\'s not the right word | -2 attempts' + white)
                            attempts -= 2
                            print(f'lives: {attempts}')
                            if attempts < 0:
                                condition = 1
                                stats()
                        else:
                            condition = 2
                            stats()
                    else:
                        print(yellow + 'skipped' + white)
                else:
                    if len(option) > 1:  # checks that you only entered 1 letter
                        print(yellow + 'enter !guess to guess the full word' + white)
                    elif option.isalpha():  # only allows letters
                        letterUsed = False  # I don't fucking know, it does something I think
                        num = 0
                        # checks if letter has been used before
                        for _ in used:
                            if option == used[num]:
                                print(yellow + f'letter {option} has already been used')
                                print('enter !used to see all used letters' + white)
                                letterUsed = True
                            num += 1

                        num = 0
                        # adds letter to its spot in hidden word
                        for _ in word:
                            if letterUsed is True:
                                pass
                            # setup for blank spots
                            elif option == word[num]:
                                temp = list(fullWord)
                                temp[num] = option
                                fullWord = ''.join(temp)
                                correct += 1
                            num += 1

                        # checks if it should take away a life
                        if option not in word and option not in used:
                            attempts -= 1

                        print(fullWord)

                        # adds letter to used list
                        if letterUsed is True:
                            pass
                        else:  # adds every letter to list
                            used.append(option)
                        if fullWord == word[:-1]:  # checks if you won
                            condition = 0
                            stats()
                        elif attempts <= 0:  # checks if you have too many wrong letters
                            condition = 1
                            stats()

                        # health color
                        if mode == '!normal':
                            if attempts >= 8:
                                print(f'lives: ' + green + f'{attempts}' + white)
                            elif 8 > attempts >= 4:
                                print(f'lives: ' + yellow + f'{attempts}' + white)
                            else:
                                print(f'lives: ' + red + f'{attempts}' + white)
                        else:
                            if attempts >= 4:
                                print(f'lives: ' + green + f'{attempts}' + white)
                            elif 4 > attempts >= 2:
                                print(f'lives: ' + yellow + f'{attempts}' + white)
                            else:
                                print(f'lives: ' + red + f'{attempts}' + white)
                        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    else:
                        print(yellow + 'you can only guess letters' + white)


        print('---< welcome to hangman >---')
        print('---<   made by: cqb13   >---\n')
        time.sleep(1)
        start() 
    




         
  
elif anamenu()
    
