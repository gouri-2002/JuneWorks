

numbers=[10,11,12,34,43,54,19,78,42]

# print number of objects in numbers

# print(len(numbers))

# print even_numbers from numbers

# for i in range(0,len(numbers)):

#     if numbers[i] %2==0:
#         print(numbers[i])


# print total of numbers

total=0

for i in range(0,len(numbers)):
    total+=numbers[i]

print(total)



# print total of odd_numbers

for i in range(0,len(numbers)):
      if numbers[i] %2!=0:
           total+=numbers[i]
print(total)




