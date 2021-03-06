# from mix_it.project.vehicle.vehicle import Vehicle
from project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        Vehicle.__init__(self, available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value + self.__fuel <= self.fuel_tank:
            self.__fuel += value
            return
        self.__fuel = 50

    def drive(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if fuel_needed <= self.__fuel:
            self.__fuel -= fuel_needed
            return f"We've enjoyed the travel!"

    def refuel(self, liters):
        try:
            self.get_capacity(self.fuel_tank, self.fuel + liters)
            self.fuel += liters
            return self.fuel
        except Exception as ex:
            return str(ex)

# car  = Car(4, 50, 3, 20)
# print(car.refuel(3))