# Создать класс и методы к нему, использовать инкапсуляцию и полиморфизм
class Creature:
    def __init__(self, alive):
        self.alive = alive

class Bird(Creature):
    def __init__(self, alive, color, children):
        super().__init__(alive)
        self.color = color
        self.__children = children

    def has_new_children(self, new_children : int):
        if new_children > 0:
            self.__children += new_children
        else:
            self.__children = self.__children

    def show_children(self):
        return self.__children

    def speak(self):
        return "Tweet"

class Dog(Creature):
    def __init__(self, alive = None, color = None):
        super().__init__(alive)
        self.color = color
    def speak(self):
        return "Bark"

titmouse = Bird("yes", "grey",5)
print(titmouse.speak())

print(titmouse.has_new_children(2))
print(titmouse.show_children())

jack = Dog("yes", "orange")
print(f"Hi! It's my dog! It's {jack.color}")
print(jack.speak())
