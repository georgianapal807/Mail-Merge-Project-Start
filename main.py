#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as file:
    letter_lines = file.readlines()

with open("./Input/Names/invited_names.txt") as names:
    list_names = names.readlines()

print(letter_lines)
print(list_names)


def replace_name(new_name):
    new_line = letter_lines[0].replace("[name]", new_name)
    new_line = new_line.replace("\n", "")
    new_line = new_line.strip()
    letter_lines[0] = new_line + "\n"


for name in list_names:
    replace_name(name)
    file_name = name.replace("\n", "")
    file_name = file_name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{file_name}.txt", mode='w') as letter:
        for line in letter_lines:
            letter.write(line)
