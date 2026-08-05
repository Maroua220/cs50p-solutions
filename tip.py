meal = input("How much was the meal? ")

tip = input("What percentage would you like to tip? ")

meal = float(meal.replace("$", ""))
tip = float(tip.replace("%", ""))

tip_amount = meal * tip / 100

print(f"${tip_amount:.2f}")
