class Employee:
    a = 1 
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
        
    @property 
    def name(self):
      return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
        o.name = "Harry Khan"

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

o = Employee()
print(o.a) # Prints the a attribute

o = Programmer()
print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)