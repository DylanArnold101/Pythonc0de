list =[]
number = input("enter as many numbers as you want the equation stops once you enter 0")
while number != 0:
    list.append(number)
    number = input("enter a number")

sum = int(0)
for i in list:
    sum += i
print(sum)