class Employee:
  lang = "hndi"
  sal = 100


raj = Employee()
raj.name = "raj"
print(raj.name, raj.sal, raj.lang)

# anu = Employee()
# anu.name = "anu"
# print(anu.name, anu.sal, anu.lang)
    
def getInfo(self):
    print("Employee name is", self.name)
    raj.getInfo()
    Employee.getInfo(raj)
    
def __init__(self, name, sal, lang):
        self.name = name
        self.salary = sal
        self.language = lang
        print("I am creating an object")
        
