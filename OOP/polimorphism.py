a=10
b=20
print(a+b)# a.__add__(b) => int.__add__(a,b)

class a:
    def f1(self,val):
        pass

obj=a()
obj.f1(20) #a.f1(obj,20)

s1 = "hello"
s2="hi"
print(s1+s2) #str.__add__(s1,s2)
