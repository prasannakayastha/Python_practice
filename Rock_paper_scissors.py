#This is a game called Rock , paper and Scissors.
#Condition of winning the game - Rock beat scissors, paper beat rock  and scissors beat paper.
#In this game, there will be two players and it is best of three game. Who  will win twice , wins the game.

import random #importing the module random

game_list=["Rock" , "Paper" , "Scissors"]# Creating the list of items which is main list.
first_list=[]#empty list
sec_list=[]#empty list


def first_name(first_player): # Function define to make a random selection from the first player
    first_sel= random.choice(game_list)
    print(first_sel)
    first_list.insert(0, first_sel)
    return first_list

def second_name(sec_player):# Function define to make a random selection from the second player.
    sec_sel=random.choice(game_list)
    print(sec_sel)
    sec_list.insert(0, sec_sel)   
    return sec_list

def main():# Main function where players choices are compare to find out the winner.
   
    if first_list[0]=="Rock" and sec_list[0]=="Scissors":
        print(first_player,"wins")
    elif first_list[0]=="Rock" and sec_list[0]=="Paper":
        print(sec_player, "wins")
    elif first_list[0]=="Paper" and sec_list[0]=="Rock":
        print(first_player, "wins")
    elif first_list[0]=="Paper" and sec_list[0]=="Scissors":  
        print(sec_player, "wins")
    elif first_list[0]=="Scissors" and sec_list[0]=="Paper": 
        print(first_player, "wins")
    elif first_list[0]=="Scissors" and sec_list[0]=="Rock":
        print(sec_player, "wins")
    elif first_list[0]==sec_list[0]:
        print("Restart")

 
first_player = input("Please enter first player name: ")# Requesting the name of the first player.
first_name(first_player)#Function call
sec_player= input("Please enter the second player name: ")#Requesting the name of the second player.
second_name(sec_player)#Function call

main()# The main function is called




#print(first_list)
#print(sec_list)
    
        