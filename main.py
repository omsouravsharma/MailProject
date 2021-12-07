PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_files:
    names = name_files.readlines()
    print(names)

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        new_letter = letter_content.replace(PLACEHOLDER, name.strip())
        with open(f"./Output/ReadyToSend/Letter_for_{name.strip()}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)


