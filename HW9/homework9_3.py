# Создать класс и методы к нему, использовать инкапсуляцию и полиморфизм

class Bird:
    def __init__(self, color, children):
        self.color = color
        self.__children = children

    def has_children(self, new_childs):
            self.__children += new_childs

    def show_children(self):
        return self.__children

    def speak(self):
        return "Tweet"

class Dog:
    def speak(self):
        return "Bark"

titmouse = Bird("grey",5)
print(titmouse.speak())

print(titmouse.has_children(2))
print(titmouse.show_children())

jack = Dog()
print(jack.speak())
