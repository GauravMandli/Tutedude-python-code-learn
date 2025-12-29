class vehicle:
    cmp="xyz"

    def __init__(self,n_wheels,n_seats,mileage):
        self.n_wheels =n_wheels
        self.n_seats =n_seats
        self.mileage = mileage
 
    def get_details(self):
        return f"this vehicle is {self.n_wheels} wheels,{self.n_seats} seats and proide a mileage of {self.mileage}"

# v1=vehicle(4,7,30)
# print(v1.get_details())

class car(vehicle):
     model="abc323"
     def __init__(self,car_type,drive_tyep,wheels,seats,mileage):
        print("init of car")
        self.car_type =car_type
        self.drive_type=drive_tyep
        super().__init__(wheels,seats,mileage)#vehicle supr ni jagyaye

c1=car("suv","menual",4,7,23)
print(c1.model)

print(c1.cmp)

print(c1.mileage)
print(c1.get_details())
print(c1.__dict__)