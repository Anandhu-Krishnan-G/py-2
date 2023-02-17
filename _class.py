class Student:
    def __init__(self,name :str,place:str,age:int) -> None:
        self.name=name
        self.age=age
        self.place=place
    
    def set_age(self,age:int):
        self.age=age

    def get_age(self):
        return self.age
    
    def display_student_details(self):
        print("name is "+self.name)
        print("place is "+self.place)
        print("age is "+str(self.age))

