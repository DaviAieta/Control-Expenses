from expense import ControlExpense
from expense import Expense

if __name__ == '__main__':
    control = ControlExpense()
    
    while True:
        print('1 - Add expense')
        print('2 - List expense')
        print('3 - Exit')
        
        option = int(input('Choose the option: '))
        if(option == 1):
            description = input('What is the name of the expense?')
            category = input('What is the expense category?')
            value = input('What is the value of the expense?')