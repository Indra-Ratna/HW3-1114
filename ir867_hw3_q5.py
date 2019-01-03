# Indra Ratna
# CS - UY 1114
# 26 Sept 2018
# Homework 3
import math
a = float(input("Please enter a value of a: "))
b = float(input("Please enter a value of b: "))
c = float(input("Please enter a value of c: "))
num_sol = ""
sol1 = 0
sol2 = 0
discriminant = math.sqrt((b**2)-(4*a*c))
if(a>0):
    if(discriminant>0):
        num_sol = " two real solutions "
        sol1 = (-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)
        sol2 = (-b-(math.sqrt((b**2)-(4*a*c))))/(2*a)
        print("This equation has "+num_sol+": x="+str(sol1)+","+str(sol2))
    elif(discriminant==0):
        num_sol = " one real solution "
        sol1 = (-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)
        print("This equation has "+num_sol+": x="+str(sol1))
    else:
        num_sol = " no real solutions "
        print("This equation has "+num_sol)
else:
    sol1 = -c/b
    print("This equation has a single real solution: x = " +str(sol1))
