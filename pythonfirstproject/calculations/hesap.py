def clmenu() :
    print("Write the numbers you want the average of.")
    note1 = int(input("\nwhat's your note?"))
    if note1 > 100 or note1 < 0: print("Wrong number. Insert a number between 0-100. ")
    else:
        if note1 > 80 : print("Your note is AA")
        elif note1 > 60 : print("Your note is BB")
        elif note1 > 55 : print("Your note is CC")
        elif note1 >= 50 : print("Your note is DD")
        elif note1 < 50 : print("u flunked gg ")