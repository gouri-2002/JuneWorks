

souce_word="CHICKEN"

target_word="HEN"

word_count={}

for char in souce_word:
    if char in word_count:
        word_count[char]+=1
    else:
        word_count[char]=1

#print(word_count)

is_kangaroo_word=True

for char in target_word:
    if char in word_count and word_count.get(char)>0:
        word_count[char]-=1
    else:
        is_kangaroo_word=False
        break
print(is_kangaroo_word)



  


