class student:
    def study(self,n_hours):
     
        print( "hello i am redeing",n_hours)

    def sports(self,sports_name):
        print(sports_name)

student1=student()
print(student1)
student1.study(3)
student1.sports("cricket")
print("---------------------------")
student2=student()
print(student1)
student2.study(4)
student2.sports("chess")