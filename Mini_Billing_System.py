#This program will give you mini groceries bill.
#create the order list with the price 
#Calculate the total amount with tax.
#Create the list of items as dictionary.
item_list=[]



def groceries_list(): # Function to create list of dictionaries of item name, pricer per kg and how much.
    while True:
        try:
            value_name=str(input("Please name of the item")) 
            value_price=float(input("Price of the item per kg"))
            value_quantity=int(input("How much do you want"))
            break   
        except ValueError:
            print("Please enter the correct value")  
          
    item_dict={}

    item_dict.update({"item_name":value_name}) # add the items keys:values to the dictionary
    item_dict.update({"item_price":value_price})
    item_dict.update({"item_quantity":value_quantity})
    return item_dict

number_of_items=int(input("Please enter the number of items"))



counter=0    # Number of items ,  in future it can be user input.
while counter<=number_of_items-1: # loop to run to add items into the list
    item=groceries_list()# assign function call to a variable.
    item_list.append(item) # instead of calling function , just add the return value to the list.
    counter+=1 # to keep loop running and break the loop.
print(item_list)# print the final list of the dictionaries.

#Printing the total price of the groceries without discount

Total_bill=0 # Assign the variable 
for items in item_list:
    Total=items["item_price"] * items["item_quantity"]# assigning the value of keys to the variable
    Total_bill=Total_bill + Total # sum of the individual price
print(f"\nTotal bill for the groceries items is :${Total_bill:.2f}") # print the total bill   

#If the total bill exceed $10 , then 10% discount will apply.

if Total_bill>=10:
    discounted_amount=Total_bill * 0.1 # 10% discount applied.
    final_bill=Total_bill-discounted_amount
    print(f"Discount of (10%) applied, ${final_bill}")  
else:
    print("Sorry no discount")         
 
for k in item_list:
    print(k)
    


