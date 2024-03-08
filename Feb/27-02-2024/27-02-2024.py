class CAU():
    Uname = None
    Password = None

    def __init__(self, o_Uname, o_Password):
        self.Uname = o_Uname
        self.Password = o_Password

    def submit(self):
        if self.Password =="Pass123":
            print("You are login sucess")
        else:
            print("Incorrect Password")

submitbutton=CAU("cau@gmail.com","Pass123")
submitbutton.submit()
localadmin=CAU("cau@gmail.com","Pass1235")
localadmin.submit()
