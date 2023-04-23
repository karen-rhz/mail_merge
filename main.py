# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
letter = open("./Input/Letters/starting_letter.txt")
# .readlines returns a text in a list of strings
body_letter = letter.readlines()
# Working with only the header.
headline_letter = body_letter[0]

# Replace the [name] placeholder with the actual name.
name = open("./Input/Names/invited_names.txt")
names = []
with open("./Input/Names/invited_names.txt") as list_of_names:
    for line in list_of_names:
        # .readline gets only 1 line from the .txt
        # .strip removes spaces from strings
        get_name = name.readline().strip()
        names.append(get_name)

final_headers = []
for person in names:
    write_name = headline_letter.replace("[name]", person)
    final_headers.append(write_name)