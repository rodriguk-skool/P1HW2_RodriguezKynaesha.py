#Kynaesha Rodriguez
#September 19, 2025
#P1HW2_RodriguezKynaesha
#This program calculates and displayes travel expenses


# ----------------Pseudocode( logic) ---------------------
# 1) Print title line "This program calculates and displays travel expenses"
# 2) Ask user for: total budget, travel destination, gas cost, accommodation cost, food cost
# 3) Compute total_expenses = gas + accommodation + food
# 4) Compute remaining = budget - total_expenses
# 5) Print a formatted "Travel Expenses" summary with:
#       Location, Initial Budget, Fuel, Accommodation, Food, Remaining Balance
# ----------------------------------------------------


print("This program calculates and displays travel expenses")

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("How much will you need for accommodation/hotel? "))
food = int(input("How much do you need for food? "))

total_expenses = gas + accommodation + food
remaining = budget - total_expenses

print("\n----------------Travel Expenses----------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("Remaining Balance:", remaining)
