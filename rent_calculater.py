# Inputs we need from user
# Total Food
# Total Rent
# Electricity unit spend
# Charge per units
# person live in room/flat

# output
# Total amount you've to pay

rent = int(input("Enter your total rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity spend = "))
charge_per_units = float(input("Enter the charge per unit = "))
persons = int(input("Enter the numbers of persons living in flat/room = "))

total_bill = electricity_spend * charge_per_units

result = (rent + food + total_bill) // persons

print("")
print("Each person will pay = ", result)



