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