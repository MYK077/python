import json
from difflib import get_close_matches

# json library
# The json library can parse JSON from strings or files. The library parses JSON into a Python dictionary or list.
parsed_data = json.load(open("data.json","r"))

# return the value to the matching key from parsed_data dict
def translate(word):
    return parsed_data[word]

# this function takes the same argument as provided to translate and return results from translate
# in str format
def output(word):
    return '\n'.join(translate(word))

user_input = input("Enter the word you want to find meaning of: ")

closed_matches = get_close_matches(user_input.lower(),parsed_data.keys(),n=3,cutoff=0.6)


if user_input.title() in parsed_data:
    print(f"The meaning {user_input} is: ")
    print(output(user_input.title()))

elif user_input.upper() in parsed_data:
    print(f"The meaning {user_input} is: ")
    print(output(user_input.upper()))

elif user_input.lower() in parsed_data:
    print(f"The meaning {user_input} is: ")
    print(output(user_input.lower()))

elif closed_matches:
    entry = input(f"Did you mean {closed_matches[0]} instead. Please enter Y or N: ")
    if entry.lower() == "y":
        print(f"{closed_matches[0]} means: ")
        print(output(closed_matches[0]))

else:
    print("The input provided by you does not exist")
