#This program is shows stopwatch
#User will enter the start , stop and reset
#I will using datetime and time function for this program
import datetime
import time
def stopwatch():
    while True:
        user_input= input("Press Enter to start the stopwatch")
        print("The stopwatch start now")
        begin= time.time()
        user_input= input("Press enter to stop")
        print("The stopwatch has stopped")
        end= time.time()
        elasped= end-begin
        elasped=int(elasped)
        print(f"the total time was= {elasped} seconds")
        user_input=input("Press enter R to reset or N to stop")
        if user_input=="N" or "n":
            break
        else:
            continue

stopwatch()

    
    


