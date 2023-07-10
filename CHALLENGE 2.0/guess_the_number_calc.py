import random


def play_guess_the_number():
    secret_number = random.randint(1, 1000)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 1000: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number!")
            break
    if attempts <= 10:
        if attempts == 10:
            print("Aha! You know the secret!")
        else:
            print("Either you know the secret or you got lucky!")
    if attempts > 10:
        print("You should be able to do better!")


def play_again():
    while True:
        play_again=input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes" :
            play_guess_the_number()
        elif play_again.lower() == "no":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


play_guess_the_number()
play_again()
