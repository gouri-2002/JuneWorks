#object oriented programming

#class [ design pattern,template,blueprint] eg:string,list,set,range

#object | instance [ real world entity]

# class className:
#     Attribute
#     methods
# eg:Car [attribute:color,wheelcount,brand   methods: accelerate,start,stop]

class employee:
    eid:int
    name:str
    age:int
    gender:str
    dept:str

def set_employee(self,id,name,age,gender,dept):
    self.id=id
    self.name=name
    self.age=age
    self.gender=gender
    self.dept=dept

    def display_employee(self):
        print(self.id,self.name,self.age,self.gender,self.dept)