
f=open("C:\\Users\\ENVY\\Desktop\\JuneWorks\\FileOperations\\land_slides.txt","r")
data=[]

for line in f: #Kerala 2018 14\n
    lst=line.rstrip("\n").split(" ") #["kerala","2019","14"]
    dic={"state":lst[0],"year":lst[1],"deaths_count":int(lst[2])}
    data.append(dic)

print(data)    

# death_per state

death_per_state={}

for dic in data:
    state=dic.get("state")
    death_count=dic.get("death_count")
    
    if state in death_per_state:
        death_per_state[state]+=death_count
    else:
        death_per_state[state]=death_count
print(death_per_state)






