class Car:
    owner = "John Doe" #class attribute
    def __init__(self,brand,colour): #method to initialize object attributes
        print(self)
        self.brand = brand #object attribute
        self.colour = colour

    def start_engine(self):
        return f"{self.brand} engine started."
    

car1 = Car("Toyota","Red") #object creation
print(car1.start_engine())
print(car1.__dict__)
print(getattr(car1,"brand"))

car2 = Car("Honda","Blue")
print(car2.start_engine())

print(car1.owner) #accessing class attribute