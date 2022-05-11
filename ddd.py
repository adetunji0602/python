from questions import quiz

class Question:
    def __init__(self, question_text, question_answer):
        self.question_text = question_text
        self.question_answer = question_answer




def main():
    questions = []
    for question in quiz:
       question_text = question["question"]
       question_answer = question["correct_answer"]
       prepared_question = Question(question_text, question_answer)
       questions.append(prepared_question)
    print("questions are now loaded", questions)

main()