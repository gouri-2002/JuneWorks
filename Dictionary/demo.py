

# dict = {key:value}
student={"name":"hima","course":"fullstack"}
print(student["course"])
print(student.keys())

student["name"]="hari"
student["place"]="kerala"
print(student)


new=student.items()
print(new)


student={"name":"hima","course":"fullstack","course":"datascience"}
print(student)

student={"name":"hima","course":"fullstack","course":"datascience"}
for i in student:
    print(student[i])
    print(i)
    print(f"{i}={student[i]}")


# update the course as fullstack in student in iteration

for i in student:
    if i=="cousre":
        student[i]="datascience"

print(student)

#delete a key "place" if it present in the dict usimg iteration

student={"name":"hima","course":"datascience","place":"kerala"}

for i in student:
    if i=="place":
        student.pop(i)
print(student)


