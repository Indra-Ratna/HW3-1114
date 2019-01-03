# Indra Ratna
# CS - UY 1114
# 26 Sept 2018
# Homework 3
import random
user = input("Please enter rock, paper, or scissors: ")
cpu = random.randint(1,3)
cpuc= ""
if(user == "rock"):
    user = 1
elif(user == "paper"):
    user = 2
elif(user == "scissors"):
    user = 3
else:
    print("enter a valid selection")

if(cpu == 1):
    cpuc = "rock"
elif(cpu == 2):
    cpuc = "paper"
else:
    cpuc = "scissors"
print("Computer selected: "+cpuc)

if(cpu>user):
    if(cpu-user!= 2):
        if(cpu == 3):
            print("Scissors beats paper. Computer wins!")
        elif(cpu ==2):
            print("Paper beats rock. Computer wins!")
    else:
        print("Rock beats scissors. You win!")
elif(user>cpu):
    if(user-cpu!=2):
        if(user ==3):
            print("Scissors beats paper. You win!")
        elif(user == 2):
            print("Paper beats rock. You win!")
    else:
        print("Rock beats scissors. Computer wins!")
elif(user==1 and cpu==1):
    print("Both players choose rock. No winner!")
elif(user ==2 and cpu ==2):
    print("Both players choose paper. No winner!")
elif(user ==3 and cpu ==3):
    print("Both players choose scissors. No winner!")
