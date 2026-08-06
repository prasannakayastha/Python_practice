#This is program shows the local and global variables in the function

def symbol(x):#function define
    y=x+1# body of the function
    print("This is local", locals())
    print("This is global", globals())
    
symbol(5)# function called

   

new_symbol=symbol
new_symbol(5)