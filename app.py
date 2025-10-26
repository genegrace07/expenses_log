import json
import datetime

class Expenses:
    def __init__(self,type,amount):
        self.type = type
        self.amount = amount
        self.expenses = "logs.json"
        self.temp_expenses_list = []
        self.date_today = str(datetime.date.today())
        self.numbering = 0
    def input(self):
        print('=========== DAILY EXPENSES ===========')
        print('Choose:\n1. Income\n2. Outcome')
        self.choosen = input('> ')
    def validate(self):
        if self.choosen == '1':
            self.expense()
        elif self.choosen == '2':
            print('test')
        else:
            print('Invalid option')
    def expense(self):
        description = input('Description: ')
        your_amounts = input('Amount: ')
        self.numbering += 1
        new_entry = {"No.":self.numbering,"Description":description,"Amount":your_amounts,"Date":self.date_today}


        try:
            with open(self.expenses, "r") as f:
                data = json.load(f)
                print(data)
        except json.JSONDecodeError:
            data = []

            data.append(new_entry)
            self.temp_expenses_list.append(data)

        with open(self.expenses, "w+") as f:
            json.dump(self.temp_expenses_list,f,indent=4)
            print(f.read())




        #print(self.temp_expenses_list) #check if storing successfully

user = Expenses(0,0)
user.input()
user.validate()

