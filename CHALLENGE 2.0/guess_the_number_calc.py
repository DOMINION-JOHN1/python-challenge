def guess():
    from random import randrange
    player= int(input("guess a number: "))
    num=randrange(1,1000)
    if player>num:
         print('Too high, try again')
    else:
         print("Too low. Try again.")
    player= int(input("guess a number: "))
    print("Congratulations! You guessed the number!")


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def guess_num():
    print('Welcome to Guess the Number!')
    num_guess=0
    while True:
        guess()
        num_guess+=1
        if num_guess <= 10:
            print("Either you know the secret or you got lucky!")
        elif num_guess > 10:
            print("You should be able to do better!")
        else:
            print("Aha! You know the secret!")
        if not replay():
            break
guess_num()