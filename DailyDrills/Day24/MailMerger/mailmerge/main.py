# Written by Abenezer
#
# MAIL MERGE PROGRAM
# This program creates personalized letters for multiple people automatically.
#
# How it works:
# 1. Reads a list of names from 'invited_names.txt' file
# 2. Reads a letter template from 'starting_letter.txt' file
# 3. For each name, it replaces [name] placeholder in the template with the actual name
# 4. Adds "Written by Abenezer" signature at the end of each letter
# 5. Saves each personalized letter as a separate file in the ReadyToSend folder
#
# Input files needed:
# - Input/Names/invited_names.txt (contains list of names, one per line)
# - Input/Letters/starting_letter.txt (contains letter template with [name] placeholder)
#
# Output: Individual letter files saved in Output/ReadyToSend/ folder
# Each file will be named: letter_for_[PersonName].txt

with open('Input/Names/invited_names.txt', 'r') as names_file:
    names = names_file.readlines()

with open('Input/Letters/starting_letter.txt', 'r') as letter_file:
    letter_template = letter_file.read()

for name in names:
    clean_name = name.strip()
    personalized_letter = letter_template.replace('[name]', clean_name)
    personalized_letter += '\n\nWritten by Abenezer'
    # Save the new letter
    with open(f'Output/ReadyToSend/letter_for_{clean_name}.txt', 'w') as output_file:
        output_file.write(personalized_letter)

print('All letters are ready!')
