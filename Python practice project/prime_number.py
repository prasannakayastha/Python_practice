#This program is to check if the number is prime or not
# Check if "n" is a prime number.

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n ,"is not a prime number.")
            break
    else:
        print(n , "is a prime number")    
        
        