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
    good_response = {1: "Very good!", 2: "Excellent!", 3: "Nice work!", 4: "Keep up the good work!"}
    bad_response = {1: "No. Please try again.", 2: "Wrong. Try once more.", 3: "Don't give up!", 4: "No. Keep trying."}
    good=good_response[randrange(1,4)]
    poor=bad_response[randrange(1,4)]
    correct_count = 0
    incorrect_count = 0

    while True:
        x, y = randrange(1, 10), randrange(1, 10)
        print(f'how much is {x} time {y}?')
        answer = x * y
        student = int(input("what is the answer "))
        if answer != student:
            print(poor)
            incorrect_count += 1
        else:
            print(good)
            correct_count += 1
            if correct_count + incorrect_count == 10:
                percentage = correct_count / (correct_count + incorrect_count)
                if percentage < 0.75:
                   print("Please ask your teacher for extra help.")
                else:
                    print("Congratulations, you are ready to go to the next level!")
                break

multi_tutor()


