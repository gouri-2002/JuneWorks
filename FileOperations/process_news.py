

f=open("C:\\Users\\ENVY\\Desktop\\JuneWorks\\FileOperations\\news.txt","r")

# word_list=[]

# for line in f:

#     word=line.rstrip("\n")#Paris Olympics 2024 Day 5 (July 31)
#     words=word.split(" ")
#     #print(words)

#     for w in words:
#         word_list.append(w)

# print(word_list)


word_list=[w for line in f for w in line.rstrip("\n").split(" ") if w!=""]
print(word_list)

#word_count={}
# for w in word_list:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)

word_count={w:word_list.count(w) for w in word_list}
print(word_count)

# def get_value(key):
#     return word_count.get(key)
# srt=sorted(word_count,key=get_value,reverse=True)
# print(srt)

srt=sorted(word_count,key=lambda key:word_count.get(key),reverse=True)
print(srt)
