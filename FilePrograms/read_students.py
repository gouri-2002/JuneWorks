

f=open("C:\\Users\\ENVY\\Desktop\\JuneWorks\\FilePrograms\\students.txt","r")
students=[]

for stud in f:
    students.append(stud.rstrip("\n"))
    
print(students)
