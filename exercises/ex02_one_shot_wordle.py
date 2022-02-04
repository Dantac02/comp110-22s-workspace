"""A wordle program with a one try feature."""

__author__: str = "730398535"

secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0

user_guess: str = input("What is your 6-letter guess? ")

if user_guess == secret:
    print(f"{GREEN_BOX}" * len(secret))
    print("Woo! You got it! ")
elif len(user_guess) != len(secret) and user_guess != secret:
    while i < 6:
        input("That was not 6 letters! Try again: ")
        i = i + 1
    print("Not quite. PLay again soon! ")
elif len(user_guess) == len(secret) or user_guess != secret:
    result: str = ""
    while i < len(secret):
        if str(user_guess[i]) == str(secret[i]):
            result = result + GREEN_BOX
            i = i + 1
        else:
            result = result + WHITE_BOX
            i = i + 1
    print(result)
    print("Not quite. PLay again soon! ")