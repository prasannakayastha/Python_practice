
x={}
user_input=input("First play Select location")
user_value=input("Select x or o")
x.update({user_input:user_value})
print(x)


def in_dict(y, b):
    global x
    if y in x.keys():
        print("Choose another location")
        x=input("Select another location")
        
        
   

in_dict(user_input, user_value)



   