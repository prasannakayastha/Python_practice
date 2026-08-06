#This is a program to generate the Fibonacci sequence less than the given number.


def fib(x):
    fib_list=[]
    a,b=0,1
    while b<x:
        fib_list.append(b)
        a,b=b,a + b
    return(fib_list)

result= fib(100)
print(result(1))
 
