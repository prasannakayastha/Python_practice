#This program will give you mini groceries bill.
#create the order list with the price 
#Calculate the total amount with tax.
#Create the list of items as dictionary.




def groceries_list(): # Function to create list of dictionaries of item name, pricer per kg and how much.
    while True:
        try:
            value_name=str(input("Please name of the item = " )) 
            value_price=float(input("Price of the item per kg = $"))
            value_quantity=int(input("How much do you want in kg = "))
            break   
        except ValueError:
            print("Please enter the correct value")  
          
    item_dict={"Item_name":value_name,
               "Item_price":value_price,
               "Item_quantity":value_quantity}
 
    return item_dict


#Printing the total price of the groceries without discount
def cal(final_list):
    Sub_total_bill=0 # Assign the variable 
    for items in final_list:
        Total=items["Item_price"] * items["Item_quantity"]# assigning the value of keys to the variable
        Sub_total_bill=Sub_total_bill + Total # sum of the individual price
    return Sub_total_bill 

def main(): 
    
    item_list=[]
    number_of_items=int(input("Please enter the number of items = "))

   # Number of items ,  in future it can be user input.
    for _ in range(number_of_items): # loop to run to add items into the list
        item=groceries_list()# assign function call to a variable.
        #print(item)
        item_list.append(item) # instead of calling function , just add the return value to the list.
     
    #print(item_list)# print the final list of the dictionaries.

    for x in item_list:# Printing the dictionary into the more readable format.
        for k , v in x.items():
            print(f"{k} = {v}")
    #If the total bill exceed $10 , then 10% discount will apply.
    
    Sub_total_bill_1=cal(item_list)
    print(f"\nTotal bill for the groceries items is :${Sub_total_bill_1:.2f}") # print the total bill 
    f=open('C:\\Users\\Owner\\Desktop\\test.txt', 'w')
    f.write(f"\nTotal bill for the groceries items is :${Sub_total_bill_1:.2f}")
    f.close()

    if Sub_total_bill_1>=10:
        discounted_amount=Sub_total_bill_1 * 0.1 # 10% discount applied.
        total_bill=Sub_total_bill_1-discounted_amount
        print(f"\nDiscount of (10%) applied = ${discounted_amount:.2f}") 
        print(f"\n Total after discount = {total_bill:.2f}")
        tax_bill=0.15*total_bill
        final_bill= total_bill+tax_bill
        
        print(f"\n 15% GST = {tax_bill:.2f}") 
        print(f"\n The final bill = {final_bill:.2f}")
    else:
        print("Sorry no discount")         
    
main()

