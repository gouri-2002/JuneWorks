#write a program to check number is palidrome or not
#121 is palindrome
#235 is not palindrome

num=int(input("enter the number"))
org=num

result=0

while(num!=0):

    digit=num%10

    result=result*10+digit

    num=num//10

print(result) 

print("palindrome" if result==org else "not palindrome")