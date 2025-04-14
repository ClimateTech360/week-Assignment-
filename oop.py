# Question 1

class Car:
    def __init__(self, make, model, fuel_level=100):
        self.make = make
        self.model = model
        self.__fuel_level = fuel_level

    def start(self):
        if self.__fuel_level > 0:
            print(f"The {self.make} {self.model} starts. 🚗")
        else:
            print(f"The {self.make} {self.model} can't start due to low fuel. ⛽")

    def drive(self):
        if self.__fuel_level > 0:
            self.__fuel_level -= 10
            print(
                f"The {self.make} {self.model} is driving. 🚙 Fuel level: {self.__fuel_level}%")
        else:
            print(
                f"The {self.make} {self.model} has no fuel left! Refuel first. ⛽")

    def refuel(self, amount):
        self.__fuel_level += amount
        if self.__fuel_level > 100:
            self.__fuel_level = 100
        print(
            f"The {self.make} {self.model} has been refueled. Fuel level: {self.__fuel_level}%")


class ElectricCar(Car):
    def drive(self):
        if self._Car__fuel_level > 0:
            self._Car__fuel_level -= 5
            print(
                f"The electric {self.make} {self.model} is silently driving. ⚡ Fuel level: {self._Car__fuel_level}%")
        else:
            print(
                f"The electric {self.make} {self.model} has no charge! Please recharge. 🔋")


gas_car = Car("Toyota", "Camry")
gas_car.start()
gas_car.drive()
gas_car.refuel(30)
gas_car.drive()

print("\n--- Electric Car Action ---\n")

ev_car = ElectricCar("Tesla", "Model S")
ev_car.start()
ev_car.drive()
ev_car.refuel(50)
ev_car.drive()

# Question 2


class Car:
    def move(self):
        print("Driving 🚗")


class Plane:
    def move(self):
        print("Flying ✈️")


class Bicycle:
    def move(self):
        print("Riding 🚲")


class Boat:
    def move(self):
        print("Sailing ⛵")


vehicles = [Car(), Plane(), Bicycle(), Boat()]

for vehicle in vehicles:
    vehicle.move()
