

list=[10,3,4,8,2,9,6]

squares=[n**2 for n in list ]
print(squares)


cubes=[n**3 for n in list ]
print(cubes)

even_numbers=[n for n in list if n%2==0]
print(even_numbers)

odd_numbers=[n for n in list if n%2!=0]
print(odd_numbers)


