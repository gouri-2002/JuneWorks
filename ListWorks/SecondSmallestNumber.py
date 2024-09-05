

# second smallest


numbers=[3,5,9,8,4,2,1]

smallest_num=numbers[-1]

second_smallest=numbers[0]


for i in numbers:

    if i < second_smallest and i < smallest_num:
        second_smallest=smallest_num
        smallest_num=i

    elif i < second_smallest and i > smallest_num:
        second_smallest=i

print(second_smallest)