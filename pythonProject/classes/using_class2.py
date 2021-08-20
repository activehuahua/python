class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError('Score must be a fload or int.')

        if value < 0 or value > 100:
            raise ValueError('Score must between 0~100')
        self._score = value


s = Student()
s.score = 100
print(s.score)
