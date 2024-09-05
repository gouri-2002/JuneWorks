

# names={"hari","hima","kavya","gouri"}
# print(names)

# s=set()
# print(type(s))

# diplicates not allowed
# elements and unordered
# cannot fetch a object using index position 
# mutable

# names={"hari","gouri","hima","anna"}
# s=set()

# names.add("kochi") #to add an element
# print(names)

# names.clear() # clear the full set and return empty
# print(names)

# names.pop() # pop any random element
# print(names) 

# names.discard("hima") # to remove an element
# print(names)

name1={"hima","gouri"}
name2={"swathy","gouri"}

# name1.update(name2) # add element from any collection to the set
# print(name1)

# name2=name1.union(name2)
# name2=name1.intersection(name2)
# name2=name1.difference(name2)
name2=name1.symmetric_difference(name2)


print(name2)



