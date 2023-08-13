import  os
from colorama import Fore , Style
class RetirementCalculator:
    def __init__(self, current_age, retirement_age, years_after_retirement,
                 annual_deposit, interest_rate, current_savings,
                 desired_retirement_income):
        self.current_age = current_age
        self.retirement_age = retirement_age
        self.years_after_retirement = years_after_retirement
        self.annual_deposit = annual_deposit
        self.interest_rate = interest_rate
        self.current_savings = current_savings
        self.desired_retirement_income = desired_retirement_income

    def calculate(self):
        int_rate = self.interest_rate / 100.0
        future_value = self.current_savings
        years_data = []

        for year in range(1, self.years_after_retirement + 1):
            last_year_plus_annual_deposit = future_value + self.annual_deposit
            interest_earned = last_year_plus_annual_deposit * int_rate
            future_value = last_year_plus_annual_deposit + interest_earned
            years_data.append(future_value)

        annual_retirement_income = future_value / self.years_after_retirement
        on_track = annual_retirement_income > self.desired_retirement_income

        print(Fore.GREEN + Style.BRIGHT+"Total Retirement Savings:", future_value)
        print(Fore.GREEN + Style.BRIGHT+"Annual Retirement Income:", annual_retirement_income)
        print(Fore.GREEN + Style.BRIGHT+"Are you on track?", "Yes" if on_track else "No")


def temp2():
    os.system("clear")
    print(Fore.BLUE + Style.BRIGHT+
    '''
██████╗ ███████╗████████╗██╗██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗           ██████╗ █████╗ ██╗      ██████╗
██╔══██╗██╔════╝╚══██╔══╝██║██╔══██╗██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝          ██╔════╝██╔══██╗██║     ██╔════╝
██████╔╝█████╗     ██║   ██║██████╔╝█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   █████╗    ██║     ███████║██║     ██║     
██╔══██╗██╔══╝     ██║   ██║██╔══██╗██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   ╚════╝    ██║     ██╔══██║██║     ██║     
██║  ██║███████╗   ██║   ██║██║  ██║███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║             ╚██████╗██║  ██║███████╗╚██████╗
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝              ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝


'''
)
    current_age = int(input("Enter your current age: "))
    retirement_age = int(input("Enter your desired retirement age: "))
    years_after_retirement = int(input("Enter the number of years after retirement: "))
    annual_deposit = float(input("Enter your annual deposit: "))
    interest_rate = float(input("Enter the annual interest rate (%): "))
    current_savings = float(input("Enter your current savings: "))
    desired_retirement_income = float(input("Enter your desired retirement income: "))

    calculator = RetirementCalculator(current_age, retirement_age, years_after_retirement, annual_deposit,
                                       interest_rate, current_savings, desired_retirement_income)
    calculator.calculate()
    k = input("PRESS ENTER TO CONTINUE")


# if __name__ == "__main__":
#     main()