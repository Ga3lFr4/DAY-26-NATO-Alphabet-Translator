import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Word to translate to NATO alphabet: ").upper()
translated = [nato_dict[letter] for letter in user_input]
print(translated)
