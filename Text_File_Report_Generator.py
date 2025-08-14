#This program is design to generate report of employee's loggings and sales.
#There are many things to be optimise like using of "sum" function instead of "+=" operator, and replacing for loop with one line code and so on.

Months=["January","February","March","April","May", "June","July", "August","September","October","November","December"]
totale_sales=[120,110,150,140,160,130,170,180,155,165,200,250]
total_revenue=[24000,22500,30000,27800,32500,25000,35000,37200,31000,33800,42000,55000]

revenue={}
for x in range(0,len(Months)):
    revenue[Months[x]]=total_revenue[x]
print(revenue) 
 
def avg_revenue_growth():
    total=0
    for item in total_revenue:
        total+=item
    avg_revenue=float(total/len(total_revenue))  
    return(avg_revenue)
    
    
def growth_revenue():
   
    def get_value(pair):
        return pair[1]
    sorted_items= sorted(revenue.items(), key=get_value)  
    sorted_dic=dict(sorted_items) 
    #print(sorted_dic)
    Highest_growth=list(sorted_dic.keys())[-1]
    lowest_growth=list(sorted_dic.keys())[0]
    print(f"This highest growth month is {Highest_growth}")
    print(f"This lowest month is {lowest_growth}")
    
       
def six_monthly_revenue():
    list_revenue=list(revenue.values())
    first_six=list_revenue[:6]
    second_six=list_revenue[6:]
    total_first_six=0
    total_sec_six=0
    for x in first_six:
        total_first_six+=x
           
    print(f"First six months revenue: ${total_first_six}")  
    for y in second_six: 
        total_sec_six+=y 
    print(f"Second six months revenue: ${total_sec_six}")
 
six_monthly_revenue()           
       
growth_revenue()    



    
avg=avg_revenue_growth()    
print(f"Average revenue is ${avg:.2f}")
   
    


    
'''   for item , revenue  in enumerate(total_revenue):
        print(f"Month {item} - ${revenue}")'''