class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

    def show_student(self):
        print("Student ID:", self.sid)
        print("Student Name:", self.name)

class Marks(Student):
    def __init__(self, sid, name, algo, ds, calc):
        super().__init__(sid, name)
        self.algo = algo
        self.ds = ds
        self.calc = calc

    def show_marks(self):
        print("Marks in Algorithm:", self.algo)
        print("Marks in Data Science:", self.ds)
        print("Marks in Calculus:", self.calc)

class Result(Marks):
    def __init__(self, sid, name, algo, ds, calc):
        super().__init__(sid, name, algo, ds, calc)

    def show_result(self):
        total = self.algo + self.ds + self.calc
        avg = total / 3
        print("Total Marks:", total)
        print("Average Marks:", avg)

r = Result(451, "Asad", 85, 90, 80)
r.show_student()
r.show_marks()
r.show_result()
