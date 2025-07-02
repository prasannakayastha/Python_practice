#This program will generate random password from taking inputs from the user.
#User will define the how many characters and what should be included.
#User will define the password
#Porgram will generate the password
##Display the password.

import random

def generate_password():
    password_collection=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    1,2,3,4,5,6,7,8,9,0]
    try: 
        user_input= int(input("How long is your password (8-12) :"))
        while user_input<8 or user_input>12:
            print("Password must between 8-12")
            user_input= int(input("How long is your password (8-12) :"))
            
        for items in password_collection[:]:
            if type(items)==int:
                items_list=str(items)
                password_collection.remove(items)
                password_collection.append(items_list)
        
        password_list=[]
        for x in range(1,user_input+1):
            password_generator= random.choice(password_collection)
            password_list.append(password_generator)
            
            password_final="".join(password_list)
    
        return password_final

    except ValueError:
        return("Invalid Input")
        
        
    
print(generate_password())


    