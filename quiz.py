import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # generate 10 random questions
        question_types = (Add, Multiply)
        for _ in range(5):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)
        # add these questions into self.questions

    def take_quiz(self):
        # log start time
        self.start_time = datetime.datetime.now()

        # ask all the questions
        for question in self.questions:
            # log if they got the question right
            self.answers.append(self.ask(question))
        else:
            # log the end time
            self.end_time = datetime.datetime.now()

        # show a summary
        return self.summary()

    def ask(self, question):
        # log the start time
        correct = False
        question_start = datetime.datetime.now()
        answer = input(question.text + ' = ')

        if answer == str(question.answer):
            correct = True

        question_end = datetime.datetime.now()
        return correct, question_end - question_start

    def total_correct(self):
        # return the total number of correct answers
        total = 0
        for answer in self.answers:
            print(answer[0])
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many you got right and the number of questions
        print("You got {} out of {} right".format(self.total_correct(), len(self.questions)))
        # print the total time of the quiz
        print("It took you {} seconds total.".format((self.end_time - self.start_time).seconds))

Quiz().take_quiz()
