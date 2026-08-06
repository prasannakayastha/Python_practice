state="OFF"

def fan_state(fan_speed):
    
    if fan_speed=="OFF":
        fan_speed="LOW"
    elif fan_speed=="LOW":
        fan_speed="MEDIUM"
    elif fan_speed=="MEDIUM":
        fan_speed="HIGH"
    elif fan_speed=="HIGH":
        fan_speed="OFF"
    print(f"Current state {fan_speed}")    
    return fan_speed               
   
state=fan_state(state)
state=fan_state(state)
state=fan_state(state)
state=fan_state(state)

    