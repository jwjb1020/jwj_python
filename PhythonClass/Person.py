class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def getName(self): 
        return self.name 
    def getAge(self): 
        return self.age

class Employee(Person):
    def __init__(self, name, age,employeeId):
        super().__init__(name, age)
        self.employeeId = employeeId
    def getId(self):
        return self.employeeId
emp = Employee("동양",65,2023)
print(emp.getName())
print(emp.getAge())
print(emp.getId())        

