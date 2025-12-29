class student:

    clg="sal"   
    dept=["mca","bca","mba"]
    def __init__(self,name,rallno,):
        print("calling initalizer",self)
        self.name=name
        self.rallno=rallno
        

    def study(self,n_hours):
     
        print( "hello i am redeing",n_hours)

    def sports(self,sports_name):
        print(sports_name)
student1=student("gaurav",2127)
print(student1.clg)
print(student1.dept)