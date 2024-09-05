num=int(input("enter the number"))
original=num

total=0

digit_count=len(str(num))

while(num!=0):

    digit=num%10
    exponent=digit**digit_count

    total=total+exponent

    num=num//10

print(total)    

# if(total==original):
#     print("armstrong")

# else:

#     print("non armstrong")

print("armstrong number" if original==total else "not armstrong")