import turtle

def triangle():
    for a in range(3):
        turtle.forward(100)
        turtle.right(120)
       
def square():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)
    
def rectangle():
        for a in range(2):
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(60)
            turtle.right(90)

def pentagon():
    for a in range(5):
        turtle.forward(100)
        turtle.right(72)     
             
def hexagon():
            for a in range(6):
                turtle.forward(100)
                turtle.right(60)

def circle():
    r = 50
    turtle.circle(r) 

  

def dwmenu() :
    print("╔═════════════════╔═════════════════════╗═════════════════╗")
    print("║═════════════════╚══════DRAWINGS═══════╝═════════════════║")
    print("║         1-  Draw Square                                 ║ ")
    print("║         2-  Draw Triangle                               ║ ")
    print("║         3-  Draw Rectangle                              ║ ")                            
    print("║         4-  Draw Circle                                 ║ ")
    print("║         5-  Draw Pentagon                               ║ ")
    print("║         6-  Draw Hexagon                                ║ ")
    print("║         e-  Exit                                        ║ ")      
    print("║                                                         ║ ")
    print("╚═════════════════════════════════════════════════════════╝ ")

    print(" What's your choice? ")

    choice = input()

    if choice == "1" : square()
    
    if choice == "2" : triangle()
    
    if choice == "3" : rectangle()
    
    if choice == "4" : circle()
    
    if choice == "5" : pentagon()
    
    if choice == "6" : hexagon()
    
    if choice == "e" or "E" : exit()
