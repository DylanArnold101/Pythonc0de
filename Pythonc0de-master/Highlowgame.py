from random import *
randomnum = randint(1,100) 
count = 0

while True:
    num = input("Guess the number")
    if (randomnum ==num):
        print("You rock")
        count+=1
        break 
    if (randomnum != num):
        print("You suck like trash") 
        count+=1
    if (randomnum < num):
        print("too high")
    if (randomnum > num):
        print("too low")

print("you took "+str(count)+" tries")