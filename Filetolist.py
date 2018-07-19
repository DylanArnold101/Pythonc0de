file = open("file.txt", "r+").read()
list = []
list.append(file)
for i in file:
    print(i)