import json
import random
import os
from colorama import Fore , Style

def askQuestion():
    os.system("clear")
    print(Fore.BLUE + Style.BRIGHT+
    '''
 ██████╗ ██╗   ██╗███████╗███████╗████████╗██╗ ██████╗ ███╗   ██╗       █████╗ ██╗██████╗ 
██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║      ██╔══██╗██║██╔══██╗
██║   ██║██║   ██║█████╗  ███████╗   ██║   ██║██║   ██║██╔██╗ ██║█████╗███████║██║██████╔╝
██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╗██║╚════╝██╔══██║██║██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚████║      ██║  ██║██║██║  ██║
 ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                                                                                          
                                        
'''
)
    # Load the questions from the JSON file
    with open('finance_questions.json', 'r') as json_file:
        questions = json.load(json_file)
    # Shuffle the questions
    random.shuffle(questions)

    # Select 10 random questions
    selected_questions = questions[:10]

    # Initialize the score
    score = 0

    # Present the quiz to the user
    for i, question_data in enumerate(selected_questions, start=1):
        question = question_data['question']
        options = question_data['options']
        answer = question_data['answer']

        print(Fore.LIGHTRED_EX + Style.BRIGHT +f"Question {i}: {question}")
        for j, option in enumerate(options, start=1):
            print(Fore.CYAN + Style.BRIGHT +f"{j}. {option}")

        user_answer = input("Your answer (enter the option number): ")
        
        # Check if the user's answer is correct
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            if options[int(user_answer) - 1] == answer:
                score += 1

    # Print the final score and correct answers
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT +f"\nQuiz completed! Your score: {score}/{len(selected_questions)}")
    print("Correct answers:")
    for i, question_data in enumerate(selected_questions, start=1):
        print(Fore.LIGHTRED_EX + Style.BRIGHT +f"Question {i}: {question_data['question']}")
        print(Fore.GREEN + Style.BRIGHT +f"Correct answer: {question_data['answer']}\n"+Fore.RESET)
    k = input("PRESS ENTER")
