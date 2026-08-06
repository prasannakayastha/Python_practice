#This is a program to play Tic Tac Toe with two players.
#Each player will take turn and who will match three circle or cross straight  will be the winner.
# I have no idea what module to use and we will make changes as we go.
#Looks like I will use dictionary to start with and see how that goes.


#how to check_win player--function to be create
#how to check player move  with loop--function to be create

updated_matrix={"A1":None,"A2":None,"A3":None,"B1":None,"B2":None,"B3":None,"C1":None,"C2":None,"C3":None}


def first_player_move():
    first_player= input( "First Player-Press o(O) or x(X) :")
    upper_first_player=first_player.lower() 
    while upper_first_player not in ["x","o"]:
        print("Invalid input, select x or o")
        first_player= input( "First Player-Press o (O) or x(X) :")
        upper_first_player=first_player.lower()
      
    user_position=input("Position (A1, A2, A3 , B1, B2, B3, C1 , C2, C3):")
    updated_matrix.update({user_position:upper_first_player})    
    print(updated_matrix)

   

def second_player_move():
    second_player=input(" Second Player-Press o or x :")
    upper_second_player=second_player.lower()
    while upper_second_player not in ["x","o"] :
        print("Invalid input, select x(X) or o(O)")
        second_player= input( "Second Player-Press o(O) or x(X) :")
        upper_second_player=second_player.lower()
        
    user_position=input("Position (A1, A2, A3 , B1, B2, B3, C1 , C2, C3):")
    updated_matrix.update({user_position:upper_second_player})
    
    print(updated_matrix)
 

def check_win():
    
    
        if updated_matrix["A1"]=="x" and updated_matrix["A2"]=="x"  and updated_matrix["A3"]=="x" :
            print ("You won")
        elif updated_matrix["B1"]=="x"  and updated_matrix["B2"]=="x"  and updated_matrix["B3"]=="x" :
            print ("You won")
        elif updated_matrix["C1"]=="x"  and updated_matrix["C2"]=="x"  and updated_matrix["C3"]=="x" :
            print ("You won")
        elif updated_matrix["A1"]=="x"  and updated_matrix["B2"]=="x" and updated_matrix["C3"]=="x" :
            print ("You won")
        elif updated_matrix["A2"]=="x"   and updated_matrix["B2"]=="x"  and updated_matrix["C2"]=="x" :
            print ("You won")
        elif updated_matrix["A1"]=="x" and updated_matrix["B1"]=="x" and updated_matrix["C1"]=="x" :
            print ("You won")
        elif updated_matrix["A2"]=="x" and updated_matrix["B2"]=="x"  and updated_matrix["C2"]=="x" :
            print ("You won")
        elif updated_matrix["A3"]=="x"  and updated_matrix["B3"]=="x"  and updated_matrix["C3"]=="x" :
            print ("You won")    
        elif updated_matrix["A1"]=="o"   and updated_matrix["A2"]=="o"  and updated_matrix["A3"]=="o" :
            print ("You won")
        elif updated_matrix["B1"]=="o"  and updated_matrix["B2"]=="o"  and updated_matrix["B3"]=="o" :
            print ("You won")
        elif updated_matrix["C1"]=="o"  and updated_matrix["C2"]=="o"  and updated_matrix["C3"]=="o" :
            print ("You won")
        elif updated_matrix["A1"]=="o"  and updated_matrix["B2"]=="o" and updated_matrix["C3"]=="o" :
            print ("You won")
        elif updated_matrix["A2"]=="o"   and updated_matrix["B2"]=="o"  and updated_matrix["C2"]=="o" :
            print ("You won")
        elif updated_matrix["A1"]=="o" and updated_matrix["B1"]=="o" and updated_matrix["C1"]=="o" :
            print ("You won")
        elif updated_matrix["A2"]=="o" and updated_matrix["B2"]=="o"  and updated_matrix["C2"]=="o" :
            print ("You won")
        elif updated_matrix["A3"]=="o"  and updated_matrix["B3"]=="o"  and updated_matrix["C3"]=="o" :
            print ("You won")    
         
 

def main():
    try:
        while True:
            first_player_move()
            check_win()
            second_player_move()
            check_win()
            print(check_win)               
                
    except KeyboardInterrupt:
        print("Game Exit")    

main() 





''' winning_comb=[["A1","A2","A3"],#column
                  
                  ["B1","B2","B3"],#column
                  
                ["C1","C2","C3"], #column
                
                ["A1","B2","C3"],#diagonal
                
                ["A3","B2","C1"],#diagonal
                
                ["A1","B1","C1"],#row
                
                ["A2","B2","C2"],#row
                
                ["A3","B3","C3"],#row
                ]
    
    
    
    
    for combo in winning_comb:
        values='''
