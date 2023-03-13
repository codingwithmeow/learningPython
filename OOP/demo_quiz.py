class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex=0

    def getQuestion(self):
        return quiz.questions[self.questionIndex]

    def displayQuestion(self):
        question=self.getQuestion()
        print(f'Soru {self.questionIndex+1} : {question.text}')

        for q in question.choices:
            print('-'+q)

        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Score:' ,self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex +1

        if questionNumber > totalQuestion:
            print('done')
        else:
            print(f'Question: {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('What is the best programming language?', ['C#','python','JAVAscript','java'],'python')
q2 = Question('What is the most popular programming language?', ['C#','python','JAVAscript','java'],'python')
q3 = Question('Which programming language is the most profitable??', ['C#','python','JAVAscript','java'],'python')

questions = [q1,q2,q3]
quiz = Quiz(questions)

quiz.loadQuestion()

