secret: str = "python"
result: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
user_guess: str = input("Give me a word! ")

if user_guess[0] == secret[0]:
    result + GREEN_BOX
else:
    result + WHITE_BOX

print(result)