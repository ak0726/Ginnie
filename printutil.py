from colorama import Fore, Style
def prc(col, str):
    print(Fore.GREEN + str + Fore.RESET)

prc("RED", "this is good")