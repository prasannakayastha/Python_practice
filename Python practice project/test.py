#This is python program perform simple mathematics calculation 

# Ask user for the numbers
def calculate():
    num1=float(input("Please enter the First number"))
    num2=float(input("Please enter the Second number"))

# Ask for the operation from the user
    operation=input("Please choose the operation +, -, x, /")

# perfrom the requested operation
    if operation=="+":
        output= num1+num2
    elif operation=="-":
        output=num1-num2
    elif operation=="x":
        output=num1*num2
    elif operation=="/":
        
        if num2==0:
            print("Error: Division by zero")
            return       
        else:
            output= num1/num2
    else:
        print("Invalid operation")
        
#Print the output
    print(f"{num1}{operation}{num2}={output}")     

calculate()
