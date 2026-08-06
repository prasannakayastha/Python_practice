
'''x=[{'item_name': 'apple', 'item_price': 2.0, 'item_quantity': 3}, 
   {'item_name': 'banana', 'item_price': 3.0, 'item_quantity': 5},
   {'item_name': 'carrot', 'item_price': 4.0, 'item_quantity': 2}]




total=0
for y in x:

    z=(y["item_price"])
    total=total+z
print("Total bill for the groceries items is :", total)'''       


    

'''while True:
    try:
        x=int(input("Please enter the number between 0 and 9 :"))
    except ValueError:
        print("Please enter the number")    
    except KeyboardInterrupt:
        print("Exit")
        break'''
        
      
      
'''x=[{'item_name': 'ap', 'item_price': 3.0, 'item_quantity': 4}, {'item_name': 'ba', 'item_price': 4.0, 'item_quantity': 5}] 

for k in x:
    for y , z in k.items():
        print(y,z)'''
        
        
'''yes_votes = 42_572_654 ; no_votes = 43_132_495
percentage=yes_votes/(yes_votes+no_votes)
print("{:-9} YES VOTES {:2.2%}".format(yes_votes,percentage))  '''    
      
'''spam={'Item_name': 'apple', 'Item_price': 2, 'Item_quantity': 3}
print("First Item : {0[Item_price]:d}".format(spam))  



    x=f.write('\nThis is too expensive')
    print(x)
    y=f.tell()
    print(y)'''
    
"""import json
with open  ('C:\\Users\\Owner\\Desktop\\test.txt', 'w') as f:
    x=[1,"prasanna","janice"]
    z=json.dump(x,f)
    
    
with open  ('C:\\Users\\Owner\\Desktop\\test.txt', 'r') as f:   
    y=json.load(f)
    print(type(y))"""
    
    
'''while True:
    try:
        user_input=int(input("Please enter the number"))
        print(user_input)
        break
    except (ValueError, KeyboardInterrupt):
        print("Ooops wrong input, please try again") '''
        
        
'''x=input("Y or y").lower()
if x=="y":
    print("lower")
elif x=="Y":
    print("upper")  '''
    
    
    
'''
 
class local(): # Create a class called local()
    
    x=5 # this is a property of that class
    
    
z=local()# Create a object called z
 
print(z.x)# print that object   
'''  
  
x="idle"    
while True:
    user_input=input("Please enter the pin code")
    if user_input=="YES":
        x="busy" 
        print(x)    
   
    
            