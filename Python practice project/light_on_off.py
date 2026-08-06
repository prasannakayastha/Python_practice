# Check the state of the light
# Change the state of the light at user request. 


#user_request=input("Do you want to turn on or turn off the light")


lights_on= False

def turn_on():
    global lights_on
    if lights_on==False:
        
        print("On")
        lights_on=True
        print(f"Current state :{lights_on}")
    else:
        print("Keep it on")
        print(f"Current state :{lights_on}")
    
def turn_off():
    global lights_on
    if lights_on==True:
        
        print("off")
        lights_on=False
        print(f"Current state :{lights_on}")
    else:
        print("Keep it off")
        print(f"Current state :{lights_on}")
    
   
        
#if user_request=="On":
turn_on()
turn_on()
    
#elif user_request=="Off":
turn_off() 
turn_off()              
turn_on()        