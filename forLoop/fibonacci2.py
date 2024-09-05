#read a number print number is fibonacci or not

number=int(input("enter the number"))

previous=0

current=1

isFibo=False

if number in (0,1):
    isFibo=True
else:
    
    next=previous+current
    
    while(next<=number):
        next=previous+current
        previous=current
        current=next
        
        if next==number:
            isFibo=True
            break
        
print(isFibo)
