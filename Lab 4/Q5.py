class Vehicle:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.__price = price
        self.available = True

    def check_availability(self):
        return self.available

    def rent(self):
        if self.available:
            self.available = False
            print(self.make, self.model, "has been rented.")
        else:
            print(self.make, self.model, "is not available.")

    def return_vehicle(self):
        self.available = True
        print(self.make, self.model, "has been returned.")

    def total_cost(self, days):
        return self.__price * days

    def show_details(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Price per day:", self.__price)
        print("Available:", self.available)


class Car(Vehicle):
    pass

class SUV(Vehicle):
    pass

class Truck(Vehicle):
    pass


class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.__contact = contact
        self.history = []

    def add_rental(self, rental):
        self.history.append(rental)

    def show_history(self):
        print("Rental History of", self.name)
        for r in self.history:
            print(r.vehicle.make, r.vehicle.model, "-", r.start, "to", r.end)


class RentalReservation:
    def __init__(self, customer, vehicle, start, end):
        self.customer = customer
        self.vehicle = vehicle
        self.start = start
        self.end = end
        self.vehicle.rent()
        customer.add_rental(self)

    def show_reservation(self):
        print("Customer:", self.customer.name)
        print("Vehicle:", self.vehicle.make, self.vehicle.model)
        print("From:", self.start, "To:", self.end)
        print("Total Cost:", self.vehicle.total_cost(5))


def show_info(obj):
    if isinstance(obj, Vehicle):
        obj.show_details()
    else:
        obj.show_reservation()


car1 = Car("Toyota", "Corolla", 5000)
suv1 = SUV("Kia", "Sportage", 8000)
truck1 = Truck("Isuzu", "D-Max", 10000)

cust1 = Customer("Ali", "03211234567")

r1 = RentalReservation(cust1, car1, "2025-10-05", "2025-10-10")

show_info(car1)
show_info(r1)

cust1.show_history()
car1.return_vehicle()
