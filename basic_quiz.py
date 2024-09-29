class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        return (self.answer).lower() == answer.lower()

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_questions(self):
        return self.questions[self.question_index]

    def display_question(self):
        siradaki_soru = self.get_questions()

        print(f"Question {self.question_index+1}: {siradaki_soru.text}")

        for q in siradaki_soru.choices:
            print("-",q)
        given_anwer = input("Your answer: ").strip()
        self.guess(given_anwer)
        self.loadQuestion()

    def guess(self,answer):
        siradaki_soru = self.get_questions()
        self.score += siradaki_soru.check_answer(answer)  # True için 1 False için 0 olur
        self.question_index += 1

    def get_score(self):
        print("Finish. Score: ",self.score)


    def loadQuestion(self):
        if(self.question_index == 0):
            print("Good Luck...")
        if len(self.questions) == self.question_index:
            self.get_score()
        else:
            self.display_progress()
            self.display_question()

    def display_progress(self):
        total_question = len(self.questions)
        current_question_number = self.question_index + 1
        if current_question_number > total_question:
            print("Finish.")
        else:
            print(f"Question {current_question_number} of {total_question}")



q1 = Question("2+2=?", ["3","4","5","6"],"4")
q2 = Question("Which is the most popular pl ?", ["C#", "Python", "Java"], "Python")
q3 = Question("What is the capital city of Turkey ? ", ["Ankara", "İstanbul"], "Ankara")
my_quiz_list = [q1,q2,q3]


quiz1 = Quiz(my_quiz_list)

quiz1.loadQuestion()


