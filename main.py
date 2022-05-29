import guessing
import hangman


def choose_game():
    print("*********************************")
    print("*******Choose your game!*******")
    print("*********************************")
    chosen_game = int(input("Hangman (1) - Guessing (2): "))

    while chosen_game not in range(1, 3):
        print("For the love o god, PLEASE, follow the goddam instructions!")
        print("*******Choose your game!*******")
        chosen_game = int(input("Hangman (1) - Guessing (2): "))

    if chosen_game == 1:
        hangman.play()
    else:
        guessing.play()


if (__name__) == "__main__":
    choose_game()
