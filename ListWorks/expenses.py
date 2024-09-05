

expenses=[12000,13000,10000,14000,15000,21000,22000,13000]

# find count of object in expenses

# expense_count=len(expenses)

# print all expenses

# for i in range(0,len(expenses)):
#     print(expenses[i])

# print expenses>15000

# for i in range(0,len(expenses)):

#     if expenses[i]>15000 :
#         print(expenses[i])



# print total expenses

total_expenses=0

for i in range(0,len(expenses)):
    
    total_expenses=total_expenses+expenses[i]
print(total_expenses)


#avg expense

average_expense=total_expenses/len(expenses)

print(average_expense)

