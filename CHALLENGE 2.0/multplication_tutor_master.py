import random
good=random.choice(["Very good!", "Excellent!", "Nice work!", "Keep up the good work!"])
fail=random.choice(["No. Please try again.", "Wrong. Try once more.", "Don't give up!", "No. Keep trying."])
def generate_question():
    num1 = random.randint(10, 999)
    num2 = random.randint(10, 999)
    question = f"How much is {num1} times {num2}? "
    answer = num1 * num2
    return question, answer

def main_game():
    num_correct = 0
    num_incorrect = 0
    print("Welcome to the multiplication game!")
    question, answer = generate_question()
    while True:
        user_input = int(input(question))
        if user_input == answer:
            print(good)
            num_correct+=1
            question, answer = generate_question()
        else:
            print(fail)
            num_incorrect+=1
            if num_correct + num_incorrect == 10:
                percentage_correct = num_correct / (num_correct + num_incorrect) * 100
                if percentage_correct < 75:
                    print("Please ask your teacher for extra help.")
                else:
                    print("Congratulations, you are ready to go to the next level!")
                    break
                break
main_game()
