

email_id=[
    "sam@gmail.com",
    "smith@gmail.com",
    "jhon@gmail.com",
    "stuart@gmail.com",
    "james@gmail.com",
]

f=open("C:\\Users\\ENVY\\Desktop\\JuneWorks\\FilePrograms\\email.txt","w")
for email in email_id:
    f.write(email+"\n")

f=open("C:\\Users\\ENVY\\Desktop\\JuneWorks\\FilePrograms\\email.txt","w")
for years in range(1800,3000):
    f.write(str(years)+"\n")