import random
import time


def print_guessed_letter(_user_guess_list):
    """Utility function to print User Guess List"""
    print("Your Secret word is: " + "".join(_user_guess_list))


def main():
    user_guess_list = []
    user_guesses = []
    play_game = True
    category = ""
    continue_game = "Y"

    name = input("Enter your name")
    print("Hello", name.capitalize(), "let's start playing Hangman!")
    time.sleep(1)
    print(
        "The objective of the game is to guess the secret word chosen by the computer."
    )
    time.sleep(1)
    print(
        "You can guess only one letter at a time. Don't forget to press 'enter key' after each guess."
    )
    time.sleep(2)
    print("Let the fun begin!")
    time.sleep(1)

    while True:
        # Choosing the Secret word
        while True:
            if category.upper() == "S":
                secret_word = random.choice(superHeroes)
                break
            elif category.upper() == "F":
                secret_word = random.choice(fruits)
                break
            else:
                category = input(
                    "Please select a valid category: F for Fruits / S for Super-Heroes; X to exit"
                )

            if category.upper() == "X":
                print("Bye. See you next time!")
                play_game = False
                break

        if play_game:
            secret_word_list = list(secret_word)
            attempts = len(secret_word) + 2

            # Adding blank lines to user_guess_list to create the blank secret word
            for n in secret_word_list:
                user_guess_list.append("_")
            print_guessed_letter(user_guess_list)

            print("The number of allowed guesses for this word is:", attempts)

            # starting the game
            while True:
                print("Guess a letter:")
                letter = input()

                if letter in user_guesses:
                    print("You already guessed this letter, try something else.")

                else:
                    attempts -= 1
                    user_guesses.append(letter)
                    if letter in secret_word_list:
                        print("Nice guess!")
                        if attempts > 0:
                            print("You have ", attempts, "guess left!")
                        for i in range(len(secret_word_list)):
                            if letter == secret_word_list[i]:
                                letter_index = i
                                user_guess_list[letter_index] = letter.upper()
                        print_guessed_letter(user_guess_list)

                    else:
                        print("Oops! Try again.")
                        if attempts > 0:
                            print("You have ", attempts, "guess left!")
                        print_guessed_letter(user_guess_list)

                # Win/loss logic for the game
                joined_list = "".join(user_guess_list)
                if joined_list.upper() == secret_word.upper():
                    print("Yay! you won.")
                    break
                elif attempts == 0:
                    print("Too many Guesses!, Sorry better luck next time.")
                    print("The secret word was: " + secret_word.upper())
                    break

            # Play again logic for the game
            continue_game = input(
                "Do you want to play again? Y to continue, any other key to quit"
            )
            if continue_game.upper() == "Y":
                category = input(
                    "Please select a valid category: F for Fruits / S for Super-Heroes"
                )
                user_guess_list = []
                user_guesses = []
                play_game = True
            else:
                print("Thank You for playing. See you next time!")
                break
        else:
            break


if __name__ == "__main__":
    fruits = [
        "pear",
        "mango",
        "apple",
        "banana",
        "apricot",
        "pineapple",
        "cantaloupe",
        "grapefruit",
    ]
    superHeroes = [
        "hawkeye",
        "robin",
        "Galactus",
        "thor",
        "mystique",
        "superman",
        "deadpool",
        "vision",
    ]

    main()
