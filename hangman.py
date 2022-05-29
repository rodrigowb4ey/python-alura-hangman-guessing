import random


def guess_a_letter():
    return input("One letter... ").strip().upper()


def load_secret_word(first_valid_line=0, file_name="words.txt"):
    word_list = []

    with open(file_name, "r") as words:
        for current_line in words:
            word_list.append(current_line.strip())

    secret_word = word_list[random.randint(first_valid_line, (len(word_list) - 1))]

    return secret_word


def show_welcome_message():
    print("******************************")
    print("Welcome to the hangman game!")
    print("******************************")


def set_amount_of_letters(secret_word):
    return ["_" for letter in secret_word]


def point_correct_guess(secret_word, your_letter, letters_you_got_right):
    index = 0
    for current_letter in secret_word:
        if your_letter == current_letter.upper():
            letters_you_got_right[index] = current_letter.upper()
        index = index + 1


def show_winning_message():
    print("Congratulations, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def show_losing_message(secret_word):
    print("Wow, you got hanged!")
    print(f"The secret word was {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def draw_gallow(number_of_chances):
    print("  _______     ")
    print(" |/      |    ")

    if number_of_chances == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if number_of_chances == 5:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if number_of_chances == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if number_of_chances == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if number_of_chances == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if number_of_chances == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if number_of_chances == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def play():
    show_welcome_message()

    number_of_chances = 7
    you_havent_gotten_it_right_yet = True
    out_of_chances = False

    secret_word = load_secret_word()

    letters_you_got_right = set_amount_of_letters(secret_word=secret_word)

    print(letters_you_got_right)

    while you_havent_gotten_it_right_yet and not out_of_chances:
        print(f"************* You have {number_of_chances} chances left")
        your_letter = guess_a_letter()

        print("YOUR LETTER IS: ", your_letter)

        if your_letter in secret_word.upper():
            point_correct_guess(
                secret_word, your_letter, letters_you_got_right
            )
        else:
            number_of_chances = number_of_chances - 1
            draw_gallow(number_of_chances)

        print(letters_you_got_right)
        current_word_str = "".join(letters_you_got_right)

        if current_word_str.upper() == secret_word.upper():
            you_havent_gotten_it_right_yet = False

        out_of_chances = number_of_chances == 0

    if not you_havent_gotten_it_right_yet:
        show_winning_message()
    else:
        show_losing_message(secret_word)


if (__name__) == "__main__":
    play()
