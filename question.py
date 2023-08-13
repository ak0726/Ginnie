import json
from colorama import Fore , Style
file = open("question.json")
x = file.read()
final = json.loads(x)

for a in final:
    # print(f"Q. {a['question']}")
    # print(f"> {a['option']['1']}")
    print(final[a])
    # print(a)
# print(final )