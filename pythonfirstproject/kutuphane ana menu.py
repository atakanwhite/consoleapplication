import newyork.newbest
import fambook.famousbooks
import magazines.magg
import calculations.hesap
def anamenu():
    print("╔═════════════════╔════════════════╗═════════════════╗")
    print("║═════════════════╚LIBRARY ARCHIVES╝═════════════════║")
    print("║         1-   Famous Books                          ║ ")
    print("║         2-   New York Best Sellers                 ║ ")
    print("║         3-   Magazines                             ║ ")                            
    print("║         4-   News                                  ║ ")
    print("║         5-   Calculations                          ║ ")
    print("║         6-   Art Books                             ║ ")
    print("║         e-   Exit                                  ║ ")
    print("╚════════════════════════════════════════════════════╝ ")

    print(" What's your choice? ")

    choice = input()

    if choice == "1" :
        fambook.famousbooks.fmmenu()
        anamenu()

    if choice == "2" :
         newyork.newbest.bsmenu()
         anamenu()
         
    if choice == "3" :
         magazines.magg.mgmenu()
         anamenu()
    if choice == "5" :
         calculations.hesap.clmenu()
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
