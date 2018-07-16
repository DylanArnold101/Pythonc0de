pennies = raw_input("how many pennies ")
float(pennies) *= 0.01
nickels = raw_input("how many nickels")
nickels *= 0.05
dimes = raw_input("how many dimes")
dimes *= 0.1
quarters = raw_input("how many quarters")
quarters *= 0.25
print("you have $"+pennies+nickels+dimes+quarters+str(u'\xa2'))