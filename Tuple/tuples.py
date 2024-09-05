



# numbers=(1,2,3,4) #tuple defined by ()

# print(numbers[1])


#numbers=[1,2,[3,(100,200,300),4],5,6]>>>>>>>>[1,2[3,4,(100,150,200,300)],5,6]

numbers=[1,2,[3,(100,200,300),4],5,6]

# num=numbers[2][1]

# new_num=list(num)

# new_num.insert(1,150)


# list_num=numbers[2]
# list_num[2].pop()
# list_num[2].insert(1,4)


# print(tuple(new_num))


# numbers[2][1]=tuple(new_num)

# print(numbers)




num=numbers[2]

four=num.pop()

num.insert(1,four)

print(num)

new_num=numbers[2][2]

l=list(new_num)

l.insert(1,150)

l1=tuple(l)

numbers[2][2]=l1

print(numbers)


