# print leap years

years=1800

while(years<=2024):

    if(years%100==0 and years%400 or years%100!=0 and years%4==0):

        print(years)

        
    years=years+1