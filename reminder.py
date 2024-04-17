import time
def countdown(t):
    task=input("enter your task")
    while t>0:
        #print(t)
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer,end='\r') 
        t=t-1
        time.sleep(1)
    print("its time to")
    print(task.upper())

t=int(input("enter the time in seconds after which you want to do yur task"))
countdown(t)    
