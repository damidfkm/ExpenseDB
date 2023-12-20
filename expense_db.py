from expense import Expense, ExpenseDatabase

# Create an instance of ExpenseDatabase
db = ExpenseDatabase()

# Add some expenses
db.add_expense("Groceries", 100.50)
db.add_expense("Rent", 500.00)
db.add_expense("Utilities", 150.00)
db.add_expense("Transportation", 90.00)
db.add_expense("AltSchoolTuition", 30.00)
db.add_expense("Internet", 130.85)

# Print all expenses
print("All expenses:")
for expense in db.to_dict():
    print(expense)

# Update an expense
first_expense_id = db.expenses[0].id
db.get_expense_by_id(first_expense_id).update(title="Groceries", amount=120.75)

# Print all expenses after update
print("\nAll expenses after update:")
for expense in db.to_dict():
    print(expense)

# Remove an expense
db.remove_expense(first_expense_id)

# Print all expenses after removal
print("\nAll expenses after removal:")
for expense in db.to_dict():
    print(expense)

# Get expenses by title
print("\nExpenses with title 'Utilities':")
for expense in db.get_expense_by_title("Utilities"):
    print(expense.to_dict())
