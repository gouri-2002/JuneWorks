

f_read=open("C:\\Users\\ENVY\\Desktop\\JuneWorks\\FileOperations\\years.txt","r")
f_century=open("C:\\Users\\ENVY\\Desktop\\JuneWorks\\FileOperations\\century.txt","w")
f_non_century=open("C:\\Users\\ENVY\\Desktop\\JuneWorks\\FileOperations\\non_century.txt","w")

for years in f_read:
    y=int(years.rstrip("\n"))
    if y%100==0:
        f_century.write(str(y)+"\n")
    else:
        f_non_century.write(str(y)+"\n")
