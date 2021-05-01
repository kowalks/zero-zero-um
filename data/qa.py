import csv
import random as rnd

class QA():
    def __init__(self, key, *args, **kwargs):
        self.generate(key)
        self.key = key
        self.question = self.read_q()
        self.ans = self.read_a()




    def generate(self, key):
        with open("q&a/ans.csv", mode='w') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # [Answer, Option B, Option C]
            x = [key - 3.5, key - 4.5, key - 5.5]
            employee_writer.writerow(x)
            x = [key - 8, key - 7, key - 9]
            employee_writer.writerow(x)
            x = [key - 32, key - 31, key - 30]
            employee_writer.writerow(x)
            # print("successfull")

    def read_q(self):
        q = []
        f = open("q&a/questions.txt", "r")
        for text in f:
            text = text.replace("\n", "") #removing \n
            q.append(text)
        f.close()

        # print("questions created")
        return q

    def read_a(self):
        a = []
        with open('q&a/ans.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a.append(row)

        # print("ans created")
        return a


    def reload(self):
        self.question = self.read_q()
        self.ans = self.read_a()

    def get_qa(self):
        if len(self.question) == 0:
            # print("it is empty")
            self.reload()
            # print("reload successfull")

        #getting them
        sort = rnd.randint(0, len(self.question)-1)
        question = self.question[sort]
        ans = self.ans[sort]

        #removing them from the list
        self.question.remove(self.question[sort])
        self.ans.remove(self.ans[sort])

        # print("pop it")
        return question, ans

    def is_correct(self, index):
        if index == 0:
            # print("CORRECT!")
            return True

        # print("ERROOOU!")
        return False