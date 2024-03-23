def crmenu() :
    print("╔═════════════════╔═════════════════════╗═════════════════╗")
    print("║═════════════════╚═════CURRENCIES══════╝═════════════════║")
    print("║         1- Dollar to TL                                 ║ ")
    print("║         2- TL to Dollar                                 ║ ")
    print("║         3- Euro to TL                                   ║ ")                            
    print("║         4- TL to Euro                                   ║ ")
    print("║         5- Manat to TL                                  ║ ")
    print("║         6- TL to Manat                                  ║ ")
    print("║                                                         ║ ")
    print("╚═════════════════════════════════════════════════════════╝ ")

    print(" What's your choice? ")

    choice = input()

    if choice == "1" :
            
        num1 = input ("Enter the amount of dollars:\t ")
            
        print(num1,"Dollars","=", (num1*32.12),"Turkish Liras")
            
     
                
    if choice == "2" :
                num1 = input ("Enter the amount of liras:\t ")
            
                print(num1,"Turkish Liras","=",(num1*0.031),"Dollars")
            
    
    if choice == "3" :
                  num1 = input ("Enter the amount of euros:\t ")
            
                  print(num1,"Euros","=",(num1*35.03),"Turkish Liras")
             
         
    if choice == "4" :
                  num1 = input ("Enter the amount of liras:\t ")
            
                  print(num1,"Turkish Liras","=",(num1*0,029),"Euros")
             
    
    if choice == "5" :
                  num1 = input ("Enter the amount of manat:\t ")
            
                  print(num1,"Manat","=",(num1*18,88),"Turkish Liras")
               
  
    if choice == "6" :
                  num1 = input ("Enter the amount of liras:\t ")
            
                  print(num1,"Turkish Liras","=",(num1*0,053),"Manat")
    else:
      crmenu()
