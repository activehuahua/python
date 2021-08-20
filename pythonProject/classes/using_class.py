class Student:
    def __init__(self,name, score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('%s %s '%(self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def set_score(self,score):
        self.__score=score

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print("bart's grade is %s " %(bart.get_grade()))
print("lisa's grade is %s " %(lisa.get_grade()))

print(bart.get_score())
bart.set_score(100)
print(bart.get_score())
print(bart.get_name())