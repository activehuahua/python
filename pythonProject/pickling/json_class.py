import  json

class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

def stu2dic(stu):
        return {
            "name":stu.name,
            "age":stu.age,
            "score":stu.score
        }


student=Student("Alex",30 ,90)
#print(json.dumps(stu2dic(student)))
#print(json.dumps(student,default=stu2dic))
print(json.dumps(student, default=lambda obj: obj.__dict__))