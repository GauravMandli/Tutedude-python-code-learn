# class wel:
#      @classmethod
#      def greet(cls):
#          print(cls) 
#          print("hello")

# w1=wel()
# w1.greet()
# print(wel)

class student:

    clg="sal"   
    dept=["mca","bca","mba"]
    def __init__(self,name,rallno,):
        print("calling initalizer",self)
        self.name=name
        self.rallno=rallno
        

    def study(self,n_hours):
     
        print( f"hello i am redeing{n_hours}")

    def sports(self,sports_name):
        print(f"{sports_name} in clg {self.clg}")

    @classmethod
    def greet(cls):
        print(cls)
        print(f"welcome to {cls.clg}")
    
    @classmethod
    def get_dept(cls):
        print("dept is {cls.clg} are:")
        for depts in cls.dept:
            print(depts)

student1=student("gaurav",21)
student1.study(2)
student1.sports("cricket")
student1.greet()
student1.get_dept()