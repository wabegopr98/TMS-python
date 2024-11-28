# Создать класс и методы к нему
class Bird:
    def __init__(self, color, living, changing_country = None):
        self.color = color
        self.living = living

    def flying(self,is_flying):
        if is_flying:
            print("This bird can fly")
        else:
            print("This bird can't fly")

    def speed(self, speed_fly):
        print (f"This bird is flying with {speed_fly}")



Vorobei = Bird("grey", "Russia", "No")
Vorobei.flying(input("Эта птица может летать? "))
Vorobei.speed("46 km/h")