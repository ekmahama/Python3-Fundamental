expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = 0
for expense in expenses:
    total += expense
print(f"You spent ${total} on lunch this week.")
print(f"You spent ${sum(expenses)} on lunch this week.")


# using range
print("Using range")
total = 0
for i in range(len(expenses)):
    total += expenses[i]
print(f"You spent ${total} on lunch this week.")

# using enumerate
print("Using enumerate")
total = 0
for i, expense in enumerate(expenses):
    print(f"Expense {i+1}: ${expense}")
    total += expense
print(f"You spent ${total} on lunch this week.")

# using while loop
print("Using while loop")
total = 0
i = 0
while i < len(expenses):
    print(f"expense {i+1}: {expenses[i]}")
    total += expenses[i]
    i += 1
print(f"You spent ${total} on lunch this week.")