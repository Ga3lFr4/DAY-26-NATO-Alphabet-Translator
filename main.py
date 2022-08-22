import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

program_is_on = True

while program_is_on:
    user_input = input("Word to translate to NATO alphabet: ").upper()
    if user_input == "STOP":
        program_is_on = False
        break
    translated = [nato_dict[letter] for letter in user_input]
    print(translated)
