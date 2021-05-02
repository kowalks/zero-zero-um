import csv
import random as rnd

class QA():
    def __init__(self, key, *args, **kwargs):
        self.key = key
        self.question = "Faca = {}. Caveira = ?"

    def get_qa(self, level):
        if level == 1:
            return self.get_qa_level1()
        if level == 2:
            return self.get_qa_level2()
        if level == 3:
            return self.get_qa_level3()
        if level == 4:
            return self.get_qa_level1()

    def get_qa_level1(self):
        faca = rnd.randint(1, self.key-1)
        question = self.question.format(faca)
        ans = []
        ans.append(str(self.key - faca))
        for i in range(0,2):
            faca = rnd.randint(1, self.key - 1)
            ans.append(str(self.key - faca))

        return question, ans

    def get_qa_level2(self):
        faca = rnd.randint(-300, 300)
        question = self.question.format(faca)
        ans = []
        ans.append(str(self.key - faca))
        for i in range(0,2):
            faca = rnd.randint(-200, 200)
            ans.append(str(self.key - faca))

        return question, ans

    def get_qa_level3(self):
        faca = round(rnd.random()*rnd.randint(-100, 100),2)
        question = self.question.format(faca)
        ans = []
        ans.append(str(round(self.key - faca,2)))
        for i in range(0,2):
            faca = round(rnd.random()*rnd.randint(-100, 100),2)
            ans.append(str(round(self.key - faca,2)))

        return question, ans

    def is_correct(self, index):
        if index == 0:
            return True

        return False