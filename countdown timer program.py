import time
my_time = int(input("Enter the time in seconds: "))
for x in range (my_time, 0, -1): #for reverse count
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print (f"{hours:02}:{minutes:02}:{seconds:02}") #for upto 2 decimal places
    time.sleep(1) #to create the time lag of one second
print ("TIME'S UP!")