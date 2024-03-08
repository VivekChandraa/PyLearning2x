class Car():
    name = None
    speed = None

    def who_is_driving(self):
        print("BMW driving by " + self.name)

    def what_is_speed(self):
        print(self.name + " Speed is 100km/h " )


Vivek_ref_name_obj = Car()
Vicky_ref_name_obj = Car()

Vivek_ref_name_obj.name = "Vivek"
Vicky_ref_name_obj.name = "Vicky"
Vivek_ref_name_obj.who_is_driving()
Vivek_ref_name_obj.what_is_speed()
print("---------------------")
Vicky_ref_name_obj.who_is_driving()
Vicky_ref_name_obj.what_is_speed()
