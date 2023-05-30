import random


def generate_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    question = f"How much is {num1} times {num2}? "
    answer = num1 * num2
    correct_answer = answer.__str__()
    return question, correct_answer


def get_response(is_correct):
    if is_correct:
        responses = ["Very good!", "Excellent!", "Nice work!", "Keep up the good work!"]
    else:
        responses = ["No. Please try again.", "Wrong. Try once more.", "Don't give up!", "No. Keep trying."]
    return random.choice(responses)


def main_game():
    print("Welcome to the multiplication game!")
    question, correct_answer = generate_question()
    while True:
        user_input = str(input(question))
        if user_input == correct_answer:
            print(get_response(True))
            question, correct_answer = generate_question()
        else:
            print(get_response(False))


main_game()
