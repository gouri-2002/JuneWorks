

# mapped list

arr=[6,7,8,9,4,3,2,10]

mapped_list=[ num+1 if num>5 else num-1 for num in arr ]
print(mapped_list)
