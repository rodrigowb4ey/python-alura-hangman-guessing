import random
from utils import set_number_of_chances


def play():
    print("******************************")
    print("Welcome to the guessing game!")
    print("******************************")

    print("Select the difficulty level:")
    difficulty_level = int(input("Easy (1) - Medium (2) - Hard (3): "))

    while (
        (difficulty_level > 3)
        or (difficulty_level < 1)
        or not isinstance(difficulty_level, int)
    ):
        print("For the love o god, PLEASE, follow the goddam instructions!")
        print("Select the difficulty level:")
        difficulty_level = int(input("Easy (1) - Medium (2) - Hard (3): "))

    you_havent_gotten_it_right_yet = True
    number_of_chances = set_number_of_chances(
        difficulty_level=difficulty_level
    )

    for round in range(1, number_of_chances + 1):
        print(f"Round #{round}")
        secret_number = random.randint(1, 10)
        your_guess_str = input("Try to guess a number (1~10): ")
        try:
            your_guess = int(your_guess_str)
        except ValueError:
            print("Now you're just being rude. Fuck off!")
            break

        while your_guess > 10 or your_guess < 1:
            print(
                "You're supposed to type an integer between the 1~10 range, asshole"
            )
            your_guess_str = input("Try to guess a number (0~10): ")
            your_guess = int(your_guess_str)

        you_got_it_right = secret_number == your_guess
        bigger = your_guess > secret_number
        smaller = your_guess < secret_number

        if you_got_it_right:
            print("You got it right lol")
            you_havent_gotten_it_right_yet = False
            break
        elif bigger:
            print(f"A little less... {secret_number}")
        elif smaller:
            print(f"A little more... {secret_number}")

    if not you_havent_gotten_it_right_yet:
        print("Congrats!")
    else:
        print("No more chances left :(")


if (__name__) == "__main__":
    play()
