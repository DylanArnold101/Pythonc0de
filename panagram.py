stringy = raw_input("enter a panagram")
def isPangram(stringy):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for i in stringy:
        if i in alphabet:
            alphabet.remove(i)
    if len(alphabet) == 0:
        return True
    else:
         return False
print(isPangram(stringy))