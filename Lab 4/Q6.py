class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculateBonus(self):
        return 0

class Manager(Employee):
    def calculateBonus(self):
        return self.salary * 0.2

    def hire(self):
        print(self.name, "is hiring a new employee.")

class Developer(Employee):
    def calculateBonus(self):
        return self.salary * 0.1

    def writeCode(self):
        print(self.name, "is writing code.")

class SeniorManager(Manager):
    def calculateBonus(self):
        return self.salary * 0.3


m = Manager("Ali", 80000)
d = Developer("Sara", 60000)
s = SeniorManager("Asad", 100000)

print(m.name, "Bonus:", m.calculateBonus())
m.hire()

print(d.name, "Bonus:", d.calculateBonus())
d.writeCode()

print(s.name, "Bonus:", s.calculateBonus())
s.hire(
