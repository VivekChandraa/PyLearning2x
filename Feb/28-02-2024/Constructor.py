class Car():
    model = None
    make = None
    Year = None
    def __init__(self,o_model,o_make,o_year):
        self.model=o_model
        self.make=o_make
        self.Year=o_year
    def engine(self):
        print("Model name of " + self.model)
        print("Model name of " + self.make)
        print("Model name of " + self.Year)

Vivek = Car("BMW","BMW","2024")
Vivek.engine()

