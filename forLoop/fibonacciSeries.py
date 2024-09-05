previous=0

currrent=1

print(f"{previous},{currrent}",end=",")

for i in range(1,11):
    
    next=previous+currrent

    print(f"{next}",end=",")

    previous=currrent

    currrent=next 
