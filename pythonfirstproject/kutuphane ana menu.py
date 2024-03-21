
import drawings.draw
import playgame.pgames
import randominfo.rinfo
import calculations.hesap
import quizshow.qshow
import currencies.curr
import calories.calory

def anamenu():
     print("╔═════════════════╔══════════════════╗═════════════════╗")
     print("║═════════════════╚PYTHON CONSOLE APP╝═════════════════║")
     print("║         1-  Play Games                               ║ ")
     print("║         2-  Calculate                                ║ ")
     print("║         3-  Draw                                     ║ ")                            
     print("║         4-  Random Info                              ║ ")
     print("║         5-  Quiz Show                                ║ ")
     print("║         6-  Currencies                               ║ ")
     print("║         7-  Calories of Foods                        ║ ")
     print("║         8-  Learn About the Developer                ║ ")
     print("║         9-  FAQ                                      ║ ")
     print("║         e-   Exit                                    ║ ")
     print("╚══════════════════════════════════════════════════════╝ ")

     print(" What's your choice? ")          

     choice = input()          

     if choice == "1" :
               playgame.pgames.pgmenu()
               anamenu()
          
     if choice == "2" :
               calculations.hesap.clmenu()
               anamenu()
          
     if choice == "3" :
               drawings.draw.dwmenu()
               anamenu()
               
     if choice == "4" :
               randominfo.rinfo.rimenu()
               anamenu()
          
     if choice == "5" :
               quizshow.qshow.qumenu()
               anamenu()
          
     if choice == "6" :
               currencies.curr.crmenu
               anamenu()
          
     if choice == "7" :
               calories.calory.calmenu()
               anamenu()
          
     if choice == "8" :
               randominfo.rinfo.rimenu()
               anamenu()
          
     if choice == "9" :
               sorulansorular.freqask.fqmenu()
               anamenu()
     
     if choice == "e" or choice == "E" : exit()
     else:
          print("You can only choose 1,2,3,4 and e.")
          anamenu()
anamenu()


     # 201 ╔
     # 205 ═
     # 187 ╗
     # 186 ║
     # 200 ╚
     # 188 ╝
     #https://drive.google.com/drive/folders/1fzxnG68VzCvC4HIsVslMmQc7IHDtXt3c
