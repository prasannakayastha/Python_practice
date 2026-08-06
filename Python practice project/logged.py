state="Logging"
pss_word= input("Please enter the password : ")
#print("You are" ,state)
def account_login(login):
   
    if login=="Logging" and pss_word!="Bat":
        login="Error"
    elif login=="Logging" and pss_word=="Bat":
        login="Logged In"    
    elif login=="Error":
        login="Logged Out"
    elif login=='Logged In':
        login="Logged Out"  
  
    print(f" status -: {login}")
    return login
state=account_login(state)  

    
            
