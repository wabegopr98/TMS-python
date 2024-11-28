# Создать класс и методы к нему, использовать инкапсуляцию, полиморфизм и наследование

class Sportsman:
    def __init__(self, gender, age, type_of_sport):
        self.gender = gender
        self.age = age
        self.__type_of_sport = type_of_sport

    def change_sport(self, new_sport):
        self.__type_of_sport = new_sport
        return "He didn't change type of sport"

    def is_greatest(self, surname, allknown = None):
        if allknown:
            return f"This is  {surname}. He is allknown"
        else:
            return f"This is  {surname}. He is not allknown"

    def can_score(self, goal = None):
        if goal:
            return "He can make difference in his type of sport"
        else:
            return "He cant make difference in his type of sport"

    def is_legend(self, is_legend = None):
        if is_legend:
            return "He is legend!"

class Footballer(Sportsman):
    def can_score(self, goal = None):
        return "He can make difference in football"

class HockeyPlayer(Sportsman):
    def can_score(self, goal = None):
        return "He can make difference in hockey"

Messi = Footballer("male", 36, "football")
print(Messi.is_greatest(" Leo Messi", "yes"))
print(Messi.can_score("yes"))

Ovechkin = HockeyPlayer("male", 39, "hockey")
print(Ovechkin.is_greatest("Alex Ovechkin", "yes"))
print(Ovechkin.can_score("yes"))
print(Ovechkin.change_sport("No"))