



# wap to return the even numbrs in a list

num=[1,2,3,4,5,6,7,8]

even_num=[]

for i in num:
    if i%2==0:

        even_num.append(i)

print(even_num)

#remove even numbers

num=[1,2,3,4,5,6,7,8]

for i in num:
    if i%2==0:

        num.remove(i)

print(num)

