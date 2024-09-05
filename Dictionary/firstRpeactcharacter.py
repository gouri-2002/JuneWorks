

text="ABDDDCCDDBB"

word_count={}

for c in text:
    if c in word_count:
        print(c,"first reccursive character")
        break
    else:
        word_count[c]=1
        