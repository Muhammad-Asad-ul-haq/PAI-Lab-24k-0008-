class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        total = super().fare()
        return total + (0.1 * total)

bus = Bus(50)
print("Total Bus Fare is:", bus.fare())
