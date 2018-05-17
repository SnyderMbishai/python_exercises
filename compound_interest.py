"""Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places."""

def compound_interest():
    deposit = float(input("Deposit amount: "))
    #period = int(input("Period :"))
    rate = 0.04
    first_year_savings = deposit + (deposit*rate)
    second_year_savings = first_year_savings + (first_year_savings*rate)
    third_year_savings = second_year_savings + (second_year_savings*rate)

    print(" savings after the first year will be %.2f \n savings after the second year will be %.2f \n savings after the third year will be %.2f"%(first_year_savings, second_year_savings, third_year_savings))

compound_interest()
