

lst=[10,20,12,40,10,10,20,65,23,12]

number_count={num:lst.count(num) for num in lst }

print(number_count)


text="hello hai hello hai hii"

words=text.split(" ")
word_count={w:words.count(words) for w in words}
print(word_count)