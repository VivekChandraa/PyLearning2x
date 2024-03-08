class Cars():
    name = None
    model= None
    make = None
    def __init__(self,o_name,o_model,o_make ):
        self.name=o_name
        self.model=o_model
        self.make=o_make
    def engine(self):
        print("My car name", self.name)
        print("My car model", self.model)
        print("My car make", self.make)

Lambo=Cars("Limborgini","V400","2024")
Lambo.engine()
Alto = Cars()
Alto.engine()

