import  threading

class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

local_school=threading.local()

def process_student():
    std=local_school.student
    print('Hello, %s %s (in %s)' % (std.name,std.age ,threading.current_thread().name))

def process_thread(student):
    local_school.student=student
    process_student()

stu1=Student('Alice',20)
stu2=Student('Bob',21)

t1=threading.Thread(target=process_thread,args=(stu1,),name='Thread-A')
t2=threading.Thread(target=process_thread,args=(stu2,),name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()