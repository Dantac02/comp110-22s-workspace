"""A Basic Take On The Hit Game Wordle."""


__author__: str = "730390535"

white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"


def contains_char(a: str, b: str) -> bool:
    # a is the word, and b is the single character. 
    """This function test weither the single char is found in a string."""
    assert len(b) == 1
    i: int = 0
    t: int = 0
    while i < len(a):
        if b[0] == a[i]:
            i = i + 1
            t = t + 1
        else:
            i = i + 1
    if t > 0:
        return True
    else: 
        return False


def emojified(a: str, b: str):
    # a is the guess, and b is the secret.
    """Function designed to return information regarding guess word and secret."""
    assert len(a) == len(b)
    i: int = 0
    t: int = 0
    result: str = ""
    while i < len(a):
        if b[i] == a[i]:
            result = result + green
            i = i + 1
        elif not a[i] not in b:
            result = result + yellow
            i = i + 1
        elif b[i] != a[i]:
            result = result + white
            i = i + 1
    print(result)


def input_guess(c: int):
    """This allows the user to make a guess the length of their input."""
    # c is the users guess.
    guess: str = input("Enter a " + str(c) + " character word: ")
    if len(guess) != c:
        while len(guess) != c:
            guess = input("That wasn't " + str(c) + " chars! Try again: ")
        return(guess)
    else:
        return(guess)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Make sure to set the secret word to your liking. 
    secret: str = "codes"
    i: int = 1
    turn: int = 1
    score: int = 0
    while i < 7:
        print("=== Turn " + str(turn) + "/6 ===")
        guess = input_guess(len(secret))
        emojified(guess, secret)
        if guess == secret:
            score = score + 1
            i = i + 5
            if turn < 6:
                turn = turn + 1
            else:
                turn = 6
        else:
            i = i + 1
            turn = turn + 1
    if score == 1:
        print("You won in " + str(turn) + "/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()