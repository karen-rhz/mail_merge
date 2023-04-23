# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
letter = open("./Input/Letters/starting_letter.txt")
# .readlines returns a text in a list of strings
body_letter = letter.readlines()
# Working with only the header.
headline_letter = body_letter[0]
