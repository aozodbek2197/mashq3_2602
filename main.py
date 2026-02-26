# 1-mashq
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

p = Person("Sara", 20)
print(p.age)
# 2-mashq
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            return False
        self._age = value
        return True

p = Person("Sara", 20)
print(p.set_age(-1)) 
print(p.set_age(21)) 
print(p.age)
# 3-mashq
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "vov vov"

print(Dog("Bobik").speak())
