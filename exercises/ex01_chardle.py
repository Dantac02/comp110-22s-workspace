"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730398535"

counting_variable: int = 0

word_choice: str = input("Enter a 5-character word: ")

if len(word_choice) != 5:
    print("Error: Word must contain 5 characters")
    exit()


letter_choice: str = input("Enter a single character: ")

if len(letter_choice) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter_choice + " in " + word_choice)

if str(letter_choice[0]) == str(word_choice[0]):
    print(letter_choice + " found at index 0 ")
    counting_variable = counting_variable + 1
if str(letter_choice[0]) == str(word_choice[1]):
    print(letter_choice + " found at index 1 ")
    counting_variable = counting_variable + 1
if str(letter_choice[0]) == str(word_choice[2]):
    print(letter_choice + " found at index 2 ")
    counting_variable = counting_variable + 1
if str(letter_choice[0]) == str(word_choice[3]):
    print(letter_choice + " found at index 3 ")
    counting_variable = counting_variable + 1
if str(letter_choice[0]) == str(word_choice[4]):
    print(letter_choice + " found at index 4 ")
    counting_variable = counting_variable + 1

if counting_variable >= 2:
    print(str(counting_variable) + " instances of " + letter_choice + " found in " + word_choice)
else:
    if counting_variable == 1:
        print("1 instance of " + letter_choice + " found in " + word_choice)
    else: 
        print("No instances of " + letter_choice + " found in " + word_choice)
