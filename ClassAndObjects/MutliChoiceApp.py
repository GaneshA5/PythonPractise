from ClassAndObjects.Questions import Question

question_prompts = [
    "What is the colour of apple?\n(a)  Red/Green (b) Purple  (c) Orange\n\n",
    "What is the colour of Banana?\n(a)  Red (b) Yellow  (c) Orange\n\n",
    "What is the colour of Strawberry?\n(a)  Cyan (b) Yellow  (c) Red\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You scored " + str(score) + " out of " + str(len(questions)))


run_test(questions)
