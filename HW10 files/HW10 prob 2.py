class Car(object):
    countCar = 0
    def __init__(self, make, model, mpg):
        self.make = make
        self.model = model
        self.mpg = mpg
        Car.countCar()
        
    def __str__(self):
        out = "The make is " + self.make + " model is " + self.model
        out = out + " miles per gallon is " + (self.mpg)
        return out

    def copyCar(self):
        newCar = Car(self.make, self.model, self.mpg)
        return newCar
    
    @staticmethod
    def carCount(self):
        Car.countCar += 1
#test

car1 = Car("toyota", "camry", '90.21')
car3 = Car('ford', 'escort', '45.88')
print(car3)
print(car1)
car2 = car1.copyCar()
print(car2)

