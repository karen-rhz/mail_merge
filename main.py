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

# Save the letters in the folder "ReadyToSend"
for n in range(len(names)):
    # body_letter is a list of strings.
    # Since there's not .replace() in a list, I have to do it in 2 lines with .pop and .insert
    body_letter.pop(0)
    body_letter.insert(0, final_headers[n])
    # Creating the new file for each name
    # It will work no matter how many names you add to the invited_names.txt
    with open(f"./Output/ReadyToSend/Letter_for_{names[n]}.txt", "w") as final_letter:
        for line in body_letter:
            final_letter.write(f"{line}")