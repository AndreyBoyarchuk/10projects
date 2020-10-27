import json
from difflib import get_close_matches

from pycparser.c_ast import While

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            "Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


def wrapper():
    while True:
        user_input = input('Say Word: or type \end: ')
        if user_input == "\end":
            print("End of program")
            break
        else:
            output = translate(user_input)
            print(output)


wrapper()
