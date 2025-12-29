#__init__()
 
class student:

    def __init__(self,name,rallno,):
        print("calling initalizer",self)
        self.name=name
        self.rallno=rallno
        

    def study(self,n_hours):
     
        print( "hello i am redeing",n_hours)

    def sports(self,sports_name):
        print(sports_name)


student1=student("gaurav",2127)
# print(student1.name,student1.rallno)
# 
student1.grade="b"

print(student1.__dict__)
#objname.attribute=value
# student1.name="gaurav"