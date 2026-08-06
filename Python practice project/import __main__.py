#This is a program for a dice game
#First we will generate the random number.
import random # import the random library 

try:   #this block of code runs until errors occurred
    while True:# Loop to run continuously
       
        num1=1
        num2=6
        first_player=input("Please enter to play the dice game")
        print(f" Name :{first_player} and press enter")
        first_ran_num=random.randint(num1, num2)
        print(f"{first_player} ", "number" ,first_ran_num)
        second_player=input("Please your name to play the dice game")
        print(f" Name: {second_player} and press enter")
        sec_ran_num=random.randint(num1, num2)
        print(f"{second_player} ", "number",sec_ran_num)
        if first_ran_num>sec_ran_num:
            print(first_player, "won")
        elif sec_ran_num>first_ran_num:
            print(second_player ,"won")
                
        
except KeyboardInterrupt: #exit the program when ctrl+c is pressed
    print("\nEXIT!!!")  
                