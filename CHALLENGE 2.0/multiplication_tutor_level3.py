import random
good = random.choice(["Very good!", "Excellent!", "Nice work!", "Keep up the good work!"])
fail = random.choice(["No. Please try again.", "Wrong. Try once more.", "Don't give up!", "No. Keep trying."])


def generate_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    question = f"How much is {num1} times {num2}? "
    answer = num1 * num2
    correct_answer = answer.__str__()
    return question, correct_answer


def main_game():
    num_correct = 0
    num_incorrect = 0
    print("Welcome to the multiplication game!")
    question, correct_answer = generate_question()
    while True:
        user_input = str(input(question))
        if user_input == correct_answer:
            print(good)
            num_correct += 1
            question, correct_answer = generate_question()
        else:
            print(fail)
            num_incorrect += 1
            if num_correct + num_incorrect == 10:
                percentage_correct = num_correct / (num_correct + num_incorrect) * 100
                if percentage_correct < 75:
                    print("Please ask your teacher for extra help.")
                else:
                    print("Congratulations, you are ready to go to the next level!")


main_game()
