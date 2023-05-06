def guess():
    from random import randrange
    player= int(input("guess a number: "))
    num=randrange(1,1000)
    if player>num:
         print('Too high, try again')
    elif player<num:
         print('Too low, try again')
    else:
        print('Congratulations, you got the number')


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



print('Welcome to Guess the Number!')
while True:
    guess()
    if not replay():
        break