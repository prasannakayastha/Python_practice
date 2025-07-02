#This is a program of a Dice game.
#In this program , there are two players and roll the dice. The player that will have higher number , that player will win.

import random

def get_name():
    Player_name=[]
    for x in range(0,2):
        name=input("Please enter your name " )
        x+=1
        Player_name.append(name)
    return Player_name[0], Player_name[1]



def roll_dice(player1, player2):
    print("PLayer one : ", player1)
    ran_num1=random.randint(1,6)
    print(f"{player1} rolled {ran_num1}")
    print("Player second: ", player2)
    ran_num2=random.randint(1,6)
    print(f"{player2} rolled {ran_num2}")
    if ran_num1>ran_num2:
        print(player1, "is a winner")
    elif ran_num1==ran_num2:
        print("Restart")
    elif ran_num2>ran_num1:
        print(player2,"is a winner")
               

    

def main():  
    name_1, name_2 =get_name() 
    print("Welcome",f"{name_1} & {name_2} !")   
 
    while True:
        roll_dice(name_1,name_2)
        user_input=input("Press Enter to continue or N to Exit:" )
        if user_input.lower()== "n":
            print("Exit")
            break
    
main()    
           
    
    
    

    








        
        
    