# Indra 
# CS - UY 1114
# 26 Sept 2018
# Homework 3

day = input("Enter the day the call started at: ")
started = float(input("Enter the time the call started at (hhmm): "))
duration = float(input("Enter the duration fo the call (in minutes): "))
rate = 0
if(day!= "Sat" and day!="Sun"):
    if (started<=800 or started >=1800):
        rate = 0.25
    else:
        rate = 0.4
else:
    rate= 0.15
cost = (rate*duration)
print("This call will cost $"+str(cost))
