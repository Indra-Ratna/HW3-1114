#Indra Ratna
#CS-UY 1114
#26 Sept 2018
#Homework 3

"""
1. When 0 is inputted, the output is:
"OK"
"Wow"
"Done"
2. When 1 is inputted, the output is:
"Zoom"
"Done"
3. When 6 is inputted, the output is
"Wow"
"Done"
4. When 8 is inputted, the output is
"Zoom"
"Done"
"""
x = int(input("Enter a number: "))
if x < 3:
    if x % 2 == 0:
        print("OK")
if x % 3 == 0:
    print("Wow")
else:
    print("Zoom")
print("Done")
