#Lambda function are quick, one-time functions that can be mapped onto a different element

#A function with 3 arguments where 'expenses' enter tracker
def add_expense(expenses, amount, category):
    #To the 'expenses' list you add a dictionary pair
    expenses.append({'amount': amount, 'category': category})

#A function with 'expenses' list as the only parameter   
def print_expenses(expenses):
    #The for loop iterates over each entry of the list
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

#A function to calculate the total amount of expenses    
def total_expenses(expenses):
    #A lambda used to make a list of the 'amount' value of the 'expenses' dictionary, the .map() makes it readable, the sum totals all entries
    return sum(map(lambda expense: expense['amount'], expenses))

#A function with the parameters 'expenses' and 'category'    
def filter_expenses_by_category(expenses, category):
    #Use lambda to make a list where expense['category'] = category within expenses
    return filter(lambda expense: expense['category'] == category, expenses)
    
#A function where entry points of interactive expense tracker
def main():
    expenses = []
    #The while loop, if the condition is TRUE, will point 1 of 5 string
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        #The .input() converts the user choice to a string
        choice = input('Enter your choice: ')

        #Conditional statements differentiate what happens with input
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()