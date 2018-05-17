
def tax_and_tip():
    meal_cost = float(input("What's the cost of the meal? "))
    tax = 0.05*meal_cost
    tip = 0.18*meal_cost
    total = meal_cost + tax + tip
    print ("Tax = $%.2f"%tax + '\n' + "Tip = $%.2f"%tip + '\n' + "Total = $%.2f"%total)

tax_and_tip()
