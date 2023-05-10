import random
good=random.choice(["Very good!", "Excellent!", "Nice work!", "Keep up the good work!"])
fail=random.choice(["No. Please try again.", "Wrong. Try once more.", "Don't give up!", "No. Keep trying."])
def generate_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    question = f"How much is {num1} times {num2}? "
    answer = num1 * num2
    return question, answer

def main():
    print("Welcome to the multiplication game!")
    question, answer = generate_question()
    while True:
        user_input = int(input(question))
        if user_input == answer:
            print(good)
            question, answer = generate_question()
        else:
            print(fail)
            break
main()
