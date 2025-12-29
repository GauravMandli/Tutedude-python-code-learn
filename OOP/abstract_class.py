from my_abstrct_class import shape

class square(shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2
    
class ract(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self.breadth
    
class circle(shape):
    def __init__(self,redius):
        self.redius=redius
    
    def area(self):
        return 3.14 * self.redius ** 2
    

sq1 = square(10)
print(sq1.area())

r1= ract(6,5)
print(r1.area())

c1=circle(10)
print(c1.area())
