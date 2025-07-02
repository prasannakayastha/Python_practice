'''Instructions:

1.Loop through numbers 1 to 20.

2.Skip all even numbers (hint: number % 2 == 0)

3.Stop the loop if the number reaches 15.

4.Print only the odd numbers before 15.'''

for n in range(1,20):
    if n%2==0:
        continue
    elif n==15:
        break
    elif n%2!=0:
        print(n, "is odd")    
        
#This is my original code, and getting use to with Break and Continue statements        