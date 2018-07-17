wordcount = input("enter a number")
print("enter "+ str (wordcount)+" word/words" )
numList = []
for i in range (0,wordcount):
    num = raw_input("enter word number "+str(i+1))
    numList.append(num)
from random import * 
rand = randint(0,int(wordcount))
print(numList[rand])
    