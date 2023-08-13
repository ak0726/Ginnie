from prettytable import PrettyTable
import os
from colorama import Fore,Style
class Expense:
    def __init__(self, type, name, date, amount, id):
        self.type = type
        self.name = name
        self.date = date
        self.amount = amount
        self.id = id

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def save_expenses_to_file(self):
        with open("expenses.txt", "w") as outFile:
            for exp in self.expenses:
                outFile.write(f"{exp.type},{exp.name},{exp.date},{exp.amount},{exp.id}\n")

    def load_expenses_from_file(self, filename):
        with open(filename, "r") as inFile:
            for line in inFile:
                exp_data = line.strip().split(",")
                exp = Expense(exp_data[0], exp_data[1], exp_data[2], float(exp_data[3]), int(exp_data[4]))
                self.expenses.append(exp)

    def add_expense(self):
        expense = Expense("", "", "", 0.0, 0)

        expense.type = input("Enter expense type: ")
        expense.name = input("Enter expense name: ")
        expense.date = input("Enter expense date: ")
        expense.amount = float(input("Enter expense amount: "))

        if expense.type and expense.name and expense.date and expense.amount > 0:
            expense.id = self.expenses[-1].id + 1 if self.expenses else 1
            self.expenses.append(expense)
            self.save_expenses_to_file()

    def show_expenses(self):
        total_expense = self.calculate_total_expenses()
        t = PrettyTable(['Type', 'Name', 'Date','Amount','ID'])
        print("Expenses:")
        for exp in self.expenses:
            t.add_row([exp.type,exp.name,exp.date,exp.amount,exp.id])
            # print("Type:", exp.type)
            # print("Name:", exp.name)
            # print("Date:", exp.date)
            # print("Amount: Rs.", exp.amount)
            # print("ID:", exp.id, "\n")
        print(t)
        print(Fore.RED + Style.BRIGHT+"Total Expense: Rs.", total_expense)

    def delete_expense(self, id_to_delete):
        self.expenses = [exp for exp in self.expenses if exp.id != id_to_delete]
        self.save_expenses_to_file()

    def get_expenses(self):
        return self.expenses

    def calculate_total_expenses(self):
        total = sum(exp.amount for exp in self.expenses)
        return total

def temp():
    os.system("clear")
    print(Fore.BLUE + Style.BRIGHT+
    '''
███████╗██╗  ██╗██████╗ ███████╗███╗   ██╗███████╗███████╗      ████████╗██████╗ ██╗  ██╗
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝████╗  ██║██╔════╝██╔════╝      ╚══██╔══╝██╔══██╗██║ ██╔╝
█████╗   ╚███╔╝ ██████╔╝█████╗  ██╔██╗ ██║███████╗█████╗  █████╗   ██║   ██████╔╝█████╔╝ 
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██║╚██╗██║╚════██║██╔══╝  ╚════╝   ██║   ██╔══██╗██╔═██╗ 
███████╗██╔╝ ██╗██║     ███████╗██║ ╚████║███████║███████╗         ██║   ██║  ██║██║  ██╗
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝         ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝


'''
)
    expense_manager = ExpenseManager()
    expense_manager.load_expenses_from_file("expenses.txt")

    while True:
        print(Fore.YELLOW + Style.BRIGHT+"1. Add Expense 😋")
        print(Fore.YELLOW + Style.BRIGHT+"2. Show Expenses")
        print(Fore.YELLOW + Style.BRIGHT+"3. Delete Expense")
        print(Fore.YELLOW + Style.BRIGHT+"4. Exit")
        choice = int(input("Enter your choice: "))
        total_expense = expense_manager.calculate_total_expenses()

        if choice == 1:
            expense_manager.add_expense()
        elif choice == 2:
            expense_manager.show_expenses()
        elif choice == 3:
            id_to_delete = int(input("Enter ID of expense to delete: "))
            expense_manager.delete_expense(id_to_delete)
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

    print(Fore.RED + Style.BRIGHT+"Expenses after exiting the program:")
    expenses = expense_manager.get_expenses()
    for exp in expenses:
        t = PrettyTable(['Type', 'Name', 'Date','Amount','ID'])
        print("Expenses:")
        for exp in expenses:
            t.add_row([exp.type,exp.name,exp.date,exp.amount,exp.id])
            # print("Type:", exp.type)
            # print("Name:", exp.name)
            # print("Date:", exp.date)
            # print("Amount: Rs.", exp.amount)
            # print("ID:", exp.id, "\n")
        print(t)
    k = input("PRESS ENTER")


