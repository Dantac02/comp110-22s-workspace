SECRET: int = 3 

print("I am thinking of an impossible number between one and five, what is it? ")
guess: int = int(input("What is your useless guess? "))

if guess == SECRET:
    print("How! Are you a magician." )
else: 
    print("Sorry, dumb and dumbmer! ")

    print("Thank you for playing ;)")