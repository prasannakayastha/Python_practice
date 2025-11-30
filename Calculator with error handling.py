'''#Start with simple calculator 
#Focus on error handling
#Next stage to calculator can perform complex calculations
#Final motive is to create real hardware of the calculator.Since it was our 2nd Year project and we never completed it so I want to complete that project by my own.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Make a separate functions for the operations(addition, substraction, division and multiplication)
'''
def add(x,y): #execute the addition operation
     return x+y 

def sub(x,y):# execute the substraction operation
    return x-y

def multi(x,y):#execute the multiplication operation
   return x*y

def div(x,y):#execute the division operation
  return x/y

def main():
    while True:
        try:   
            first_num=int(input("Please enter the first number: "))
            user_operation=input("Please enter the operation + , - , x , /")
            second_num=int(input("Please enter the second number: "))
        
        except (ValueError, TypeError, NameError, ZeroDivisionError) as e:
            print(f"The error has occured {e}, Please enter the right input!")
            continue
        if user_operation=="+":
            addition=add(first_num,second_num)
            print(f" Result = {addition:.2f}")
        elif user_operation=="-":
            substraction=sub(first_num,second_num)
            print(f"Result = {substraction:.2f}")
        elif user_operation=="x":
            multiplication=multi(first_num,second_num) 
            print(f"Result = {multiplication:.2f}") 
        elif user_operation=="/" and second_num!=0:
            division = div(first_num, second_num)
            print(f"Result = {division:.2f}") 
        elif user_operation=="/" and second_num==0:
            print("Cannot be zero!")    
        else:
            print("Invalid operation", "please start again.")
            continue    
        user_input=input("Do you want to continue , press Y for Yes or N for No ")   
        user=user_input.lower()
        if user=="y":
            continue
        else:
            print("Exit")
            break

main() 









    
            











