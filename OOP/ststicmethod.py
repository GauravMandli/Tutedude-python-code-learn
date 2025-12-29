"""static metho- define inside class wichis neither bound to object nor to class to create a stitc method we use static decorator """


class student:

    clg="sal"   
    dept=["mca","bca","mba"]
    def __init__(self,name,rallno,):
        print("calling initalizer",self)
        self.name=name
        self.rallno=rallno
        

    def study(self,n_hours):
        print(self)
        print( f"hello i am {self.name} redeing{n_hours}")

    def sports(self,sports_name):
        print(f"{sports_name} in clg {self.clg}")

    @staticmethod
    def greet():
        print(f"welcome to")
    
    @classmethod
    def get_dept(cls):
        print(f"dept is {cls.clg} are:")
        for depts in cls.dept:
            print(depts)

student1=student("gaurav",21)
student1.study(3)
student1.get_dept()
student1.greet()

