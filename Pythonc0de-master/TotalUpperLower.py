Stringy = raw_input("  Enter upper and lowercase letters ")
C = int(0)
L = int(0)
for i in Stringy:
    if i.isupper():
        C+=1
    if i.islower():
        L+=1
print("you have "+str(C)+" Uppercase letters " )
print("you have "+str(L)+" Lowercase letters " )