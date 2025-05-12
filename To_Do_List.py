#This is a program for to-do-list 

to_do_list=[]# Create the empty list
num_task=int(input("How many tasks you want to do: "))# Ask user input for number of task to be add.
num_to_do_list=0 # creating a variable with initial value 0.
while num_to_do_list<num_task:# While loop continues until all the tasks are entered.
    task=input(f"Enter the task to complete {num_to_do_list +1 }: ")# Using f String to print the vaule inside the curly brackets
    to_do_list.append(task)# adding value to the list
    num_to_do_list+=1 # increament the task counter
'''to_do_list.sort()    # to sort the least by alphabetical order '''  

for x in range(len(to_do_list)):# this is will iterate the indices of the list
    print(x+1,"-", to_do_list[x], end=" ")# wrtites the value of the argument given
    



'''for i ,task in  enumerate(to_do_list):# iterate the list of the task
    print(f"{i+1}.{task}", end=" ")#print function writes the value of the argument given.'''




   
