import random
good = random.choice(["Very good!", "Excellent!", "Nice work!", "Keep up the good work!"])
fail = random.choice(["No. Please try again.", "Wrong. Try once more.", "Don't give up!", "No. Keep trying."])


def problem_type():
    print("Please select a problem type:")
    print("1 - Addition problems only")
    print("2 - Subtraction problems only")
    print("3 - Multiplication problems only")
    print("4 - Division problems only")
    print("5 - Mixture of all problem types")
    return int(input('choose an option'))


def get_difficulty_level():
    print("Please select a difficulty level:")
    print("1 - Single-digit problems only")
    print("2 - Two-digit problems")
    print("3 -  three-digit problems")
    return int(input('choose an option '))


def generate_question(difficulty, problem):
    if difficulty == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif difficulty == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif difficulty == 3:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)

    if problem == 1:
        question = f"How much is {num1} plus {num2}?"
        answer = (num1 + num2)

    elif problem == 2:
        question = f"How much is {num1} minus {num2}?"
        answer = (num1 - num2)

    elif problem == 3:
        question = f"How much is {num1} times {num2}?"
        answer = (num1 * num2)

    elif problem == 4:
        question = f"How much is {num1} divided by {num2}?( to 2 decimal place)"
        answer = round(num1 / num2, 2)

    else:
        question = f" {num1} plus {num2} times {num1} all minus {num1} divide by {num2}?"
        answer = (((num1 + num2) * num1) - num1 // num2)
    return question, answer


def main():
    num_correct = 0
    num_incorrect = 0
    print("Welcome to the multiplication game!")
    problem = problem_type()
    difficulty = get_difficulty_level()
    question, answer = generate_question(difficulty, problem)
    while True:
        print(question)
        try:
            user_input = float(input())
        except ValueError:
            print("Invalid input. Please round your answer to decimal place.")

        if user_input == answer:
            print(good)
            num_correct += 1
            question, answer = generate_question(difficulty, problem)
        else:
            print(fail)
            num_incorrect += 1
            if num_correct + num_incorrect == 10:
                percentage_correct = num_correct / (num_correct + num_incorrect) * 100
                if percentage_correct < 75:
                    print("Please ask your teacher for extra help.")
                else:
                    print("Congratulations, you are ready to go to the next level!")
                    break
                break


main()
