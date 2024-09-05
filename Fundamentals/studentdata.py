#write a program to read student name and 3 marks mark1,mark2,mark3 and print total mark and average mark

student_name=input("enter the student name")
mark1=input("enter mark1")
mark2=input("enter mark2")
mark3=input("enter mark3")

totalmark=int(mark1)+int(mark2)+int(mark3)
print(f"total marks={totalmark}")

averagemark=totalmark/3
print(f"average mark={averagemark}")
 