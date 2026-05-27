# This is a simple program how ATM machine works.
# This will check card inserted or not in first place.
# In second place, it will check what transaction has been completed.
# Depending upon those requirement , the state of the machine changes.

#insert_card()        → IDLE → CARD INSERTED
#enter_pin()          → CARD INSERTED → CHECK PIN
#check_pin()          → → VALID / ERROR
#process_transaction()→ → WITHDRAW / ERROR




    
ATM_state="IDLE"
card_pincode="123"  
min_balance=int(2000)   
    
def insert_card(state):
    if state=="IDLE":
        state="CARD INSERTED"
        return state
    else:
        state="IDLE"
        return state 
       
        
def enter_pins(state): 
    if state=="CARD INSERTED":
        card_pincode=input("Please enter the pin: ")
        if card_pincode=="123":
           state="TRANSACTION"
           return state
        elif card_pincode!="123":
            state="ERROR"
            print(state)
            return state
         
         
def check_balance(state):
    if state=="TRANSACTION":
        user_input=int(input("Please enter the amount : "))
        if user_input<=min_balance:
            state="WITHDRAW"
            return state
        else:
            state="ERROR"    
            return state
    
def cash_out(state):
    state=="WITHDRAW"
    print("Cash out")
    state="IDLE"
    return state

           
           
           
           
            
       
ATM_state=insert_card(ATM_state)
print(ATM_state) 
ATM_state=enter_pins(ATM_state)   
print(ATM_state)
ATM_state=check_balance(ATM_state)
print(ATM_state)
ATM_state=cash_out(ATM_state)
print(ATM_state)
                 