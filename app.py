from expense import ControlExpense
from expense import Expense

if __name__ == '__main__':
    control = ControlExpense()
    
    while True:
        print('1 - Add expense')
        print('2 - List expense')
        print('3 - Remove expense')
        print('4 - Exit')
        print('-'*50)
        
        option = int(input('Choose the option: '))
        if(option == 1):
            description = input('What is the name of the expense?: ')
            category = input('What is the expense category?: ')
            value = input('What is the value of the expense?: ')
            
            expense = Expense(description, category, value)
            control.append(expense)
            print('product added successfully.')
            print('-'*50)
        
        elif(option == 2):
            print('Listing products')
            print('-'*50)
            control.list_()
        
        elif(option == 3):
            index = int(input('Type expense index: '))
            control.remove(index)
        
        elif(option == 4):
            print('Leaving...')
            break