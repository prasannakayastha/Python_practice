#Another python program for stopwatch

import time

def set_time():
    input("Press Enter to start")
    start_time=time.time()
    input("Press enter to stop")
    end_time=time.time()

    elasped_time=end_time-start_time
    print(f"Elasped time:{elasped_time:.2f} sec")

if __name__=="__main__":
    set_time()    
