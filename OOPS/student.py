class student:
    name:str
    age:int
    address:str
    contact:str
    course:str
    gender:str

def set_student(self,name,age,address,contact,course,gender):

    self.name=name
    self.age=age
    self.address=address
    self.contact=contact
    self.course=course
    self.gender=gender

    def display_student(self):
        print(self.name,self.age,self.address,self.contact,self.course,self.gender)  

#create object

student_instance=student()
student_instance.set_student("hari",24,"adress khno9","django",6466447655,"male")
student_instance.display_student()