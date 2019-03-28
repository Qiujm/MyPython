# 在控制台输入3组个人信息，每个人有姓名和年龄，将信息存入字典中，将字典存入列表。
# 遍历列表，打印每个人的信息，打印格式如下：
# 1 张三 20
# 2 李四 22
# 3 王五 23

info_dict1 = {'张三':'20'}
info_dict2 = {'李四':'22'}
info_dict3 = {'王五':'23'}
lyst=[info_dict1,info_dict2,info_dict3]
# print(lyst)
i=0
for item in lyst:
    for key in item:
        print("%d %s %s" %((i+1),key,item[key]))

    i+=1

# j=0
# while j<len(lyst):
#     for key in lyst[j]:
#         print("%d %s %s" % ((j + 1), key, lyst[j][key]))
#
#     j += 1