


mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

#print all mobile_names

mobile_names=[mob.get("title") for mob in mobiles ]
#print(mobile_names)

#print all brands

brands=[mob.get("brand") for mob in mobiles ]
#print(set(brands))

brands={mob.get("brand") for mob in mobiles }
#print(brands)

#print samsung mobiles name

samsung_mobiles=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
#print(samsung_mobiles)


#print all mobiles available in range of 23k to 40k

mobiles=[mob.get("title") for mob in mobiles if mob.get("price") in range(23000,40001)]
#print(mobiles)


# max_price=0
# for mob in mobile_names:
#     if mob.get("price") > max_price:
#         max_price=mob.get("price")

# max_mob_price=[mob.get("title") for mob in mobiles if mob.get("price")==max_price]
#print(max_mob_price)

# max_price=[mob.get("title") for mob in mobiles if mob.get("price") ]
# print(max_price )


def get_price(mob):

    return mob.get("price")
costly_mobile=max(mobiles,key=get_price)
print(costly_mobile)

lowest_mobile=min(mobiles,key=get_price)
print(lowest_mobile)

#sort the price


sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)
print(sorted_mobiles)


#sum of price is not possible.it wiilnot take key value.

total=sum([mob.get("price") for mob in mobiles ])
print(total)

#same way min and max adukkm...sum placil max and min kodukknm...
#but student detail with mark venm ankil matte rithi cheyynm.





