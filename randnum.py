#This is a python program generate random numbers
import random
def ran_cal():
    num1=int(input("Please enter the start number"))
    num2=int(input("Please enter the stop number"))
    #       count_num=int(input("Please enter count"))
    ran_num= random.randint(num1, num2)
    print(ran_num)


ran_cal()
