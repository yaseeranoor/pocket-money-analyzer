print("================================")
print("      POCKET-MONEY ANALYZER")
print("================================")

money = int(input("Enter your pocket money: "))

print("Your pocket money is:", money)

expenses = []
categories = []

for i in range(5):
    category = input("Enter expense category: ")
    expense = int(input("Enter expense amount: "))

    categories.append(category)
    expenses.append(expense)

print("\n----- EXPENSE DETAILS -----")

for i in range(5):
    print(categories[i], ":", expenses[i])

highest = max(expenses)
lowest = min(expenses)

position = expenses.index(highest)

print("Most expensive category:", categories[position])

count = 0

for expense in expenses:
    if expense >= 200:
        count = count + 1

print("Expenses of ₹200 or more:", count)

total = sum(expenses)

print("\nTotal expense:", total)

remaining = money - total

print("Remaining pocket money:", remaining)

if remaining > 500:
    print("Status: You are managing your money well!")

elif remaining > 0:
    print("Status: Be careful with your spending.")

else:
    print("Status: You have exceeded your budget.")

average = total / len(expenses)

print("Average expense:", average)

print("Highest expense:", highest)

print("Lowest expense:", lowest)

sorted_expenses = sorted(expenses)

print("Expenses from lowest to highest:", sorted_expenses)

print("\n================================")
print("        FINAL MONEY REPORT")
print("================================")

print("Pocket Money     :", money)
print("Total Spent      :", total)
print("Remaining Money  :", remaining)
print("Average Expense  :", average)
print("Highest Expense  :", highest)
print("Lowest Expense   :", lowest)
print("Most Spent On    :", categories[position])
print("Expensive Items  :", count)
print("Sorted Expenses  :", sorted_expenses)

print("================================")
print("       END OF ANALYSIS")
print("================================")