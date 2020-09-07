# Example 01
class SimpleGradebook:
    def __init__(self):
        self._grades= {}
    
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grade(self, name, score):
        self._grades[name].append(score)
    
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 95)
book.report_grade('Isaac Newton', 85)

print(book.average_grade('Isaac Newton'))

from collections import defaultdict

# Example 02
class BySubjectGradebook:
    def __init__(self):
        self._grades = {} # 外側のリスト
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list) # 内側のリスト