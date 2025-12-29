class rec:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def __add__(self,other):
        return self.length + other.length  #r1.length+r2.length
r1=rec(3,5)
r2=rec(8,9)

print(r1.area())
print(r2.area())

print(r1+r2)  #ractangle.__add__(r1,r2)

