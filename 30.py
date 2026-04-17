class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Student(Person):
    def __init__(self, fname, lname, roll):
        super().__init__(fname, lname)
        self.roll = roll

p1 = Person("Ali", "Mulla")
s1 = Student("Eli","Shane", 5805)
print(s1.fname, s1.lname, s1.roll)