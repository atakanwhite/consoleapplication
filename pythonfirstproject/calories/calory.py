def calmenu() : 
    print("╔═════════════════╔══════════════════════╗════════════════╗")
    print("║═════════════════╚═══════CALORIES═══════╝════════════════║")
    print("║         1- Hamburger                                    ║ ")
    print("║         2- 1 Pizza Slice                                ║ ")
    print("║         3- 330ml Coca Cola                              ║ ")                            
    print("║         4- 1 Eti Browni                                 ║ ")
    print("║         5- 1 White Mocha                                ║ ")
    print("║         6- 1 Filter Coffee                              ║ ")
    print("║                                                         ║ ")
    print("╚═════════════════════════════════════════════════════════╝ ")

    print(" What's your choice? ")

    choice = input()

    if choice == "1" :
        print("A typical burger contains about 4 ounces of ground beef, which, according to the USDA, is 375 calories.")
    
    if choice == "2" :
      print("An average slice of pizza consists of 266 calories.")
    
    if choice == "3" :
      print("A 330ml Coca Cola consists of 37.5 calories.")  
         
    if choice == "4" :
      print("1 Eti Browni consists of 464 calories.")
    
    if choice == "5" :
      print("A 100gr White Mocha consists of 110 calories.")   
  
    if choice == "6" :
      print("A 100ml Filter Coffee consist of only 0.5 calories.")

    else: 
       return calmenu()