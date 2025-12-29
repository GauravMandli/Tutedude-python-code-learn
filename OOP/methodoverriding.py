#runtime polimorphism


class employ:
    def wh(self):
        return 45

class intern(employ):
    def wh(self):
        return 40

emp=intern()
print(emp.wh())