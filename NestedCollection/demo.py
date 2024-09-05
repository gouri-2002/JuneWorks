


arr=[
    [10,20],
    [23,45],
    [11,17]
]


numbers=[]
for lst in arr:
    for num in lst:
        numbers.append(num)
        print(num)
    print(sum(numbers))    
    

numbers=[num for lst in arr for num in lst ]   
print(sum(numbers))


evens=[num for lst in arr for num in lst if num%2==0]   
print(evens)


num_gt_15=[ num for lst in arr for num in lst if num>15 ]
print(num_gt_15)







