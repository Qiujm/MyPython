# for value in range(1,5):
#     print(value)
# for value in range(1,5.5):
#     print(value)

# values1=range(1,5)
# values2=list(range(1,5))
# print(values1,values2)

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# print("%.2f%%" %12.345)

# cars=["a","b","c","d"]
# for car in cars:
#     if car.__eq__("b"):
#         print(cars.index(car))
#     else:
#         print(car)
#
# a=1
# b=2
# if a==1 & b==2:
#     print("right")
# else:
#     print("wrong")

# table_availables=["a","b","c","d","e"]
# table_reqs=["c","e","f"]
# for table_req in table_reqs:
#     if table_req in table_availables:
#         print("find " + table_req + ";",end="")
#         # print("\n")
#     else:
#         print("sorry,no " + table_req)
#
# fav_lan={"jen":"py","sarah":'c',"phil":"ruby"}
# # print(fav_lan.items())
# friends=["sarah","tom"]
# # print(type(fav_lan.keys()))
# # print(fav_lan.keys())
# # print(fav_lan.values())
#
# for name in friends:
#     # print(fav_lan.keys())
#     if  name in fav_lan:
#         print( name + " like " + fav_lan[name].title())

list1=['alice', 'brian', 'candace']
# print(list1.__len__())
list2=[]
index=0
while index < list1.__len__():
    print(list1[index])
    list2.append(list1[index])
    index+=1
print(list2)
