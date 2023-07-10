import random


def generate_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    question = f"How much is {num1} times {num2}? "
    answer = num1 * num2
    correct_answer = answer.__str__()
    return question, correct_answer


def main_game():
    print("Welcome to the multiplication game!")
    question, correct_answer = generate_question()
    while True:
        user_input = str(input(question))
        if user_input == correct_answer:
            print("Very good!")
            question, correct_answer = generate_question()
        else:
            print("No. Please try again.")


main_game()
