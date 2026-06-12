from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

dog = Dog()
print(dog.make_sound())


class Bank(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass
    @abstractmethod
    def get_bank_name(self):
        pass

class SBI(Bank):
    def get_interest_rate(self):
        return 5.5
    def get_bank_name(self):
        return "State Bank of India"
sbi = SBI()
print(sbi.get_bank_name())
print(sbi.get_interest_rate())