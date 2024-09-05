#create a function nth_digit_max with two parameter num1,num2
#nth_digit_max(123,450)=123


def nth_digit_max(num1,num2):

    digit1=num1%10
    digit2=num2%10

    if digit1 > digit2:

        return num1 
    else:
        return num2 
    
print(nth_digit_max(129,765))    

