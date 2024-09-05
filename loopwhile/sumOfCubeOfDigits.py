num=int(input("enter thr number"))

total=0

while(num!=0):

    digit=num%10
    cube=digit**3

    total=total+cube

    num=num//10

print(total)
     