times = input("how many items are you going to collect from a list")
list =[]
for i in range(0,times):
    feedback = raw_input("enter an item in a list")
    list.append(feedback)
file = open("file.txt", "wt")
for i in list:
    file.write(i)

