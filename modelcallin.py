import os 
from colorama import Fore , Style
import subprocess
def calling():
    os.system("clear")
    print(Fore.BLUE + Style.BRIGHT+
        '''
 ██████╗ ██╗███╗   ██╗███╗   ██╗██╗███████╗
██╔════╝ ██║████╗  ██║████╗  ██║██║██╔════╝
██║  ███╗██║██╔██╗ ██║██╔██╗ ██║██║█████╗  
██║   ██║██║██║╚██╗██║██║╚██╗██║██║██╔══╝  
╚██████╔╝██║██║ ╚████║██║ ╚████║██║███████╗
 ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚══════╝


'''
    )
    while True:
        qu = input("Please enter your query or exit > ")
        if qu == 'exit':
            break
        useless_cat_call = subprocess.run(["conda activate GINN2; python3 /Users/ayushkhurana/Downloads/GINN_COPY/privateGPT.py"], 
                                    stdout=subprocess.PIPE, 
                                    text=True,
                                    shell=True, 
                                    input=qu)

        print(useless_cat_call.stdout) 
        # subprocess.run("pwd")
        k = input("Press enter to continue")

# calling()
    # /Users/ayushkhurana/Downloads/Ginn copy/privateGPT.py
    # os.system('python3 /Users/ayushkhurana/Downloads/EmbedAI-main/server/privateGPT.py')