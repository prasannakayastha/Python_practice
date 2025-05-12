#This is a program to generate the Fibonacci sequence less than the given number.

user_input= int(input("Please enter the number"))
fib_list=[]
a,b=0,1
while b<user_input:
    fib_list.append(b)
    a,b=b,a + b
print(fib_list)

    