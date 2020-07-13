from model.Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        super().__init__("car")
