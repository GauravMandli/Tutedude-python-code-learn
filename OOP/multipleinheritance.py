class a:
    def state_1(self):
        print("state 1 present")
    
    def state_2(self):
        print("state 2 present")

    def state_3(self):
        print("state 3 present")
    
class b:
    def state_4(self):
        print("state 4 present")
    
    def state_5(self):
        print("state 5 present")

class c(a,b):
    def state_6(self):
        print("state 6 present")
    
    def state_7(self):
        print("state 7 present")

cd=c()
cd.state_4()
cd.state_1()