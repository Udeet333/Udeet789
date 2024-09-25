class Car:
    def _init_(self, color, model, year):
        self.color = color
        self.model = model
        self.model = year 
    def vehical(self):
        print(f"{self.color}")
        print(f"{self.model}")
        print(f"{self.year}")

car1 = Car("black")
car2 = Car("tesla model s")
car3 = Car(2024)

car1.drive()
car2.drive()
car3.drive()   
