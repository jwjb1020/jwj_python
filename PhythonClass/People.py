class People:
    def introMe(sef):
        print("Name :", self.__name, "age :", str(self.__age))
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age =get_age
        else: 
            print("잘못된 나이")
    def get_name(self):
        return    
    

class Teacher(People):
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school
def showSchool(self):
    print("My School is ", self.school)

t = Teacher(35,"kim","high school")
t.introMe()
t.set_name("lee")
t.introMe
t.showSchool()