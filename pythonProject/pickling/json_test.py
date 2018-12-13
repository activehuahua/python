import json


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_score(self, score):
        self.score = score

def jstr2student(jstr):
    s = Student(jstr['name'], jstr['age'])
    s.set_score(jstr['score'])
    return s

json_str = '{"name": "xiaoming", "score": 10, "age": 22}'
s = json.loads(json_str, object_hook=jstr2student)
print(s)
print(s.__dict__)