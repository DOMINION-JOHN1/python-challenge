import random


def get_response(is_correct):
    if is_correct:
        responses = ["Very good!", "Excellent!", "Nice work!", "Keep up the good work!"]
    else:
        responses = ["No. Please try again.", "Wrong. Try once more.", "Don't give up!", "No. Keep trying."]
    return random.choice(responses)


def get_difficulty_level():
    print("Please select a difficulty level:")
    print("1 - Single-digit problems only")
    print("2 - Two-digits and Three-digits problems")
    return int(input('choose an option '))


def generate_question(difficulty):
    if difficulty == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    if difficulty == 2:
        num1 = random.randint(10, 1000)
        num2 = random.randint(10, 1000)
    question = f"How much is {num1} times {num2}? "
    answer = num1 * num2
    correct_answer = answer.__str__()
    return question, correct_answer


def main_game():
    num_correct = 0
    num_incorrect = 0
    print("Welcome to the multiplication game!")
    difficulty = get_difficulty_level()
    question, correct_answer = generate_question(difficulty)
    while True:
        user_input = str(input(question))
        if user_input == correct_answer:
            print(get_response(True))
            num_correct += 1
            question, correct_answer = generate_question(difficulty)
        else:
            print(get_response(False))
            num_incorrect += 1
            if num_correct + num_incorrect == 10:
                percentage_correct = num_correct / (num_correct + num_incorrect) * 100
                if percentage_correct < 75:
                    print("Please ask your teacher for extra help.")
                else:
                    print("Congratulations, you are ready to go to the next level!")
                    break
                break


main_game()
