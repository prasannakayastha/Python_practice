import time



current_light="Red"

while True:
    print(f"The current light is {current_light}")   
    if current_light=="Red":
        current_light="Yellow"
    elif current_light=="Yellow":
        current_light="Green"
        
    elif current_light=="Green":
        current_light="Red"
    print(f"The current light is {current_light}")      

    time.sleep(2)