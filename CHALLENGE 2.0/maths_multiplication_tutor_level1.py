import random

def generate_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    question = f"How much is {num1} times {num2}? "
    answer = num1 * num2
    return question, answer

def main_game():
    print("Welcome to the multiplication game!")
    question, answer = generate_question()
    while True:
        user_input = int(input(question))
        if user_input == answer:
            print("Very good!")
            question, answer = generate_question()
        else:
            print("No. Please try again.")
            break
main_game()
