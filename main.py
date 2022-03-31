import random
import string

flag = string
count_c = 0
count_u = 0
def randNO():
    randOM = random.randint(1, 3)
    if randOM == 1:
        return 's'
    elif randOM == 2:
        return 'p'
    elif randOM == 3:
        return 'c'

def Win_result(comp, you):
    if(comp == 's' and you == 'c'):
        return "False"
    elif(comp == 's' and you == 'p'):
        return "True"
    elif(comp == 'p' and you == 's'):
        return "False"
    elif(comp == 'p' and you == 'c'):
        return "True"
    elif(comp == 'c' and you == 'p'):
        return "False"
    elif(comp == 'c' and you == 's'):
        return "True"
    elif(comp == 's' and you == 's'):
        return "None"
    elif(comp == 'p' and you == 'p'):
        return "None"
    elif(comp == 'c' and you == 'c'):
        return "None"

n = int(input("Enter number of rounds you want to play with computer: "))
while(n>0):
    comp = randNO()
    print("Comp's turn, Comp selected it's outcome!")
    you = input("Your turn, Select among Stone(s), Paper(p), Scissor(c)! ")
    flag = Win_result(comp, you)
    print("Computer selected ",comp)
    if flag == "True":
        print("You won this round!")
        count_u += 1
        n -= 1
    elif flag == "False":
        print("You lost this round!")
        count_c += 1
        n -= 1
    elif flag == "None":
        print("This round, tied!!")
    
    print("Computer = "+str(count_c)+"  You = "+str(count_u))

if count_u > count_c:
    print("CONGRATULATIONS!! YOU WON THE SERIES!!")
elif count_u < count_c:
    print("You Lost the series!")
elif count_u == count_c:
    print("Series Tied!!")