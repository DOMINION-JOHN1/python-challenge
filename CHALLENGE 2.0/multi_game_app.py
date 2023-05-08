import random
from random import randrange
def repeat():
    x, y = randrange(1, 10), randrange(1, 10)
    print(f'how much is {x} time {y}?')
    answer = x * y
    student = int(input("what is the answer "))
    x, y = randrange(1, 10), randrange(1, 10)
    print(f'how much is {x} time {y}?')
    answer = x * y
    student = int(input("what is the answer "))
    if answer == student:
        print('very good')
        repeat()
    else:
        print('No,please try again')


def multi_tutor():
    x, y = randrange(1, 10), randrange(1, 10)
    print(f'how much is {x} time {y}?')
    answer = x * y
    student = int(input("what is the answer "))
    if answer == student:
        print('very good')
        repeat()
    else:
        print('No,please try again')


multi_tutor()