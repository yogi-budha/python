

class Vehicle:
    def __init__(self,setting_capacity):
        self.setting_capacity = setting_capacity
    
    def fare(self):
        return self.setting_capacity *100

class Bus(Vehicle):
    def __init__(self,setting_capacity = 50):
        super().__init__(setting_capacity)
    
    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (base_fare * 0.1)
        return total_fare

bus = Bus()
print(bus.setting_capacity)

print("Total Bus fare is : ",bus.fare())