#access modifiers in python 
# public -> var , _protected -> _var , __private -> __var

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self._age = age
        self.__salary = salary


    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,salary):
        self.__salary = salary




emp = Employee("John",30,50000)
print(emp.salary)
emp.salary = 60000
print(emp.salary) # still 50000 because __salary is private and cannot be accessed directly
