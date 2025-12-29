class vehicle:
    cmp="xyz"

    def __init__(self,n_wheels,n_seats,mileage):
        self.n_wheels =n_wheels
        self.n_seats =n_seats
        self.mileage = mileage
 
    def get_details(self):
        return f"this vehicle is {self.n_wheels} wheels,{self.n_seats} seats and proide a mileage of {self.mileage}"


class car(vehicle):
    model="abc323"
    def __init__(self,car_type,drive_tyep,wheels,seats,mileage,):
        print("init of car")
        self.car_type =car_type
        self.drive_type=drive_tyep
        super().__init__(wheels,seats,mileage)#vehicle supr ni jagyaye
    
    def disply_info(self):
        print(f"car type: {self.car_type},drive type: {self.drive_type}")
    


class elccar(car):
    def __init__(self,car_type,drive_type,wheels,seats,mileage,battery_capacity,distance_range):
        self.battery_capacity=battery_capacity
        self.distance_range=distance_range
        super().__init__(car_type,drive_type,wheels,seats,mileage)

    def charge(self):
        print(f"charging to{self.battery_capacity}")

ec1=elccar("sedan","mannual",4,5,35,100,400)
print(ec1.__dict__)