import csv

class QA():
    def __init__(self, *args, **kwargs):
        self.question = self.read_q()
        self.ans = self.read_a()


    def read_q(self):
        q = []
        f = open("q&a/questions.txt", "r")
        for text in f:
            q.append(text)
        f.close()
        return q

    def read_a(self):
        a = []
        with open('q&a/ans.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a.append(row)

        return a
