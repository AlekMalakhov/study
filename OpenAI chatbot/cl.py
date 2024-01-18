class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        def read_odometer(self):
            print(f"This car has {self.odometer_reading} miles on it.")
            pass


my_new_car = Car('audi', 'a4', 2019)
my_new_car.odometer_reading = 25
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
