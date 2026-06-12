#single inheritance

class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"
    
class dog(animal):
    #method overriding
    def speak(self):
        return super().speak() + " and I am a dog"
    
animal1 = animal("Dog")
print(animal1.name)
print(animal1.speak())
dog1 = dog("Buddy")
print(dog1.name)
print(dog1.speak())

#multilevel inheritance

class Grandparent:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am a grandparent"

class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return super().speak() + f" and I am {self.age} years old"

class Child(Parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def speak(self):
        return super().speak() + f" and I am in grade {self.grade}"

grandparent1 = Grandparent("Alice")
parent1 = Parent("Bob", 40)
child1 = Child("Charlie", 10, 5)

print(grandparent1.speak())
print(parent1.speak())
print(child1.speak())

#herarchical inheritance

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return "I am driving a vehicle"
    
class Car(Vehicle):
    def drive(self):
        return super().drive() + " and I am a car"
class Bike(Vehicle):
    def drive(self):
        return super().drive() + " and I am a bike"
    

car1 = Car("Toyota")
bike1 = Bike("Honda") 
print(car1.brand)
print(car1.drive())
print(bike1.brand)
print(bike1.drive())

#multiple inheritance

class Father:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am a father"
    

class Mother:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am a mother"
    

class Child(Father, Mother):
    def __init__(self, name, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name

    def speak(self):
        return Father.speak(self) + " and " + Mother.speak(self) + f" and I am a child named {self.name}"
    
child1 = Child("Charlie", "Bob", "Alice")
print(child1.speak())

print(Child.__mro__) #method resolution order