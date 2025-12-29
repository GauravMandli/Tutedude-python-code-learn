#compiletime polimorphisam
class a:
    def add(self,num1,num2):
        return num1+num2
    
    def add(self,num1,num2,num3):
        return num1+num2+num3
    
obj =a()
print(obj.add(10,20))