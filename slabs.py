import math
from colorama import Fore , Style

def calTax():  
    print(Fore.BLUE + Style.BRIGHT+
    '''
████████╗██████╗  █████╗  ██████╗██╗  ██╗      ████████╗ █████╗ ██╗  ██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝      ╚══██╔══╝██╔══██╗╚██╗██╔╝
   ██║   ██████╔╝███████║██║     █████╔╝ █████╗   ██║   ███████║ ╚███╔╝ 
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ╚════╝   ██║   ██╔══██║ ██╔██╗ 
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗         ██║   ██║  ██║██╔╝ ██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝         ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                        

'''
)
    age = int(input("Enter your age: "))
    tax = 0
    income = 0
    salary = float(input("Please enter your salary: "))

    if age >= 80:
        if salary <= 300000:
            tax = 0
            income = salary
        elif salary <= 500000:
            tax = 0.05 * salary
            income = salary - tax
        elif salary <= 750000:
            tax = 0.10 * salary
            income = salary - tax
        elif salary <= 1000000:
            tax = 0.15 * salary
            income = salary - tax
        elif salary <= 1250000:
            tax = 0.20 * salary
            income = salary - tax
        elif salary <= 1500000:
                tax = 0.25 * salary
                income = salary - tax
        else:
                tax = 0.30 * salary
                tax -= 0.04 * tax
                income = salary - tax
    else:
        if age < 18:
            print(Fore.RED + Style.BRIGHT+"You are not eligible to pay tax")
        else:
            if salary <= 250000:
                tax = 0
                income = salary
            elif salary <= 500000:
                tax = 0.05 * salary
                income = salary - tax
            elif salary <= 750000:
                tax = 0.10 * salary
                income = salary - tax
            elif salary <= 1000000:
                tax = 0.15 * salary
                income = salary - tax
            elif salary <= 1250000:
                tax = 0.20 * salary
                income = salary - tax
            elif salary <= 1500000:
                tax = 0.25 * salary
                income = salary - tax
            else:
                tax = 0.30 * salary
                tax -= 0.04 * tax
                income = salary - tax

    print(Fore.GREEN + Style.BRIGHT+"Total tax paid by you must be around:", tax)
    print(Fore.GREEN + Style.BRIGHT+"Total income left:", income)
    if tax!=0:
        print(Fore.GREEN + Style.BRIGHT+"You can save tax by investing the taxable amount in PF, PPF, Life insurance premium, tax-saving mutual funds, etc.")
    k = input("PRESS ENTER")
