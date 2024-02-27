class Cars():
    name = None
    model = None
    make = None

    def __init__(self, o_name, o_model, o_make):
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def engine(self):
        print("this is name of", self.name)
        print("this is name of", self.model)
        print("this is name of", self.make)


lambo = Cars("lambo", "V4", "2024")
BMW = Cars("BMW", "BMW 800", "2021")
lambo.engine()
BMW.engine() 
