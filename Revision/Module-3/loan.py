# Get details of loain
money_owed = float(input("How much do you owe?\n"))
apr = float(input("What is the annual percentage of the loan?\n"))
monthly_payments = float(
    input("How much will you pay off each month in USD?\n"))
months = int(input("How many months do you want to see the results for?\n"))

monthly_rate = (apr/100)/12
for m in range(months):
    interest_paid = money_owed*monthly_rate
    money_owed = money_owed + interest_paid - monthly_payments

    if money_owed - monthly_payments < 0:
        print(f"Your last payment is {money_owed}")
        print(f"You paid of the loan in {m+1} months.")
        break

    print(
        f"Paid ${monthly_payments} of which ${interest_paid: .2f} was interest")
    print(f"Now I owe {money_owed : .2f}")
