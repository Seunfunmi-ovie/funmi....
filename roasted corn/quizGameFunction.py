def getQuestion(quizGame):
    score = 0
    question_num = 1

    for items in quizGame:

        print(f"\nQuestion {question_num}: {items['question']}")

        for option in items['option']:
            print(option)

        pickAnswer = input("Enter Your Answer: ").upper()

        while (pickAnswer != "A" and
               pickAnswer != "B" and
               pickAnswer != "C" and
               pickAnswer != "D"):
            print("Invalid input")
            pickAnswer = input("Enter Your Answer: ").upper()

        if pickAnswer == items["answer"]:
            print("Correct")
            score += 1
        else:
            print("Incorrect Answer: The Correct Answer is", items["answer"])

        question_num += 1

    return score


def main():
    quizGame = [
        {"question": "What is the capital of Nigeria?",
         "option": ["A, Abuja", "B, Lagos", "C, Sabo", "D, London"],
         "answer": "A"},

        {"question": "What is capital of Lagos State?",
         "option": ["A, Ikorodu", "B, Ikeja", "C, Magodo", "D, Ilesa"],
         "answer": "B"},

        {"question": "Which planet is closest to the Sun?",
         "option": ["A) Venus", "B) Earth", "C) Mercury", "D) Mars"],
         "answer": "C"},

        {"question": "What is the largest ocean on Earth?",
         "option": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
         "answer": "D"},

        {"question": "How many colors are there in a rainbow?",
         "option": ["A) 6", "B) 7", "C) 8", "D) 9"],
         "answer": "B"},

        {"question": "Which animal is known as the fastest land mammal?",
         "option": ["A) Lion", "B) Cheetah", "C) Leopard", "D) Gazelle"],
         "answer": "B"},

        {"question": "What is the chemical symbol for water?",
         "option": ["A) CO2", "B) O2", "C) H2O", "D) NaCl"],
         "answer": "C"},

        {"question": "Which country is home to the kangaroo?",
         "option": ["A) South Africa", "B) Australia", "C) Brazil", "D) India"],
         "answer": "B"},

        {"question": "What is the hardest natural substance on Earth?",
         "option": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
         "answer": "C"},

        {"question": "How many continents are there on Earth?",
         "option": ["A) 5", "B) 6", "C) 7", "D) 8"],
         "answer": "C"},

        {"question": "Which instrument is used to measure temperature?",
         "option": ["A) Barometer", "B) Thermometer", "C) Odometer", "D) Speedometer"],
         "answer": "B"},

        {"question": "What is the primary gas found in the air we breathe?",
         "option": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
         "answer": "C"}
    ]

    score = getQuestion(quizGame)
    print("\nYour total score is:", score)



main()
