class Expense:
    def __init__(self, description, category, value):
        self.description = description
        self.category = category
        self.value = value
        
class ControlExpense:
    def __init__(self):
        self.expenses = []
        
    def append(self, expense):
        self.expenses.append(expense)
        
    def list_(self):
        if self.expenses:
            for index, expense in enumerate(self.expenses, start=1):
                print(f'{index}. Description: {expense.description}')
                print(f'Category: {expense.category}')
                print(f'Value: R${expense.value}')
                print('-'*50)
        else:
            print('No registered expenses')
            
    def remove(self, index):
        self.expenses.pop(index)