# Get details of a loan and calculate the monthly payment
money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What will your monthly payment be, in dollars?\n"))
months = int(input("How many months will it take to pay off the loan?\n"))

montly_rate = apr / 100 / 12

for i in range(months):
    interest = money_owed * montly_rate
    if payment > money_owed + interest:
        print(f"That's the last payment. You are now debt free.")
        break
    money_owed -= payment - interest
    print(f"Month {i+1}: Paid {payment}, of which {interest} was interest. Now I owe {money_owed}.")