# i = 1
# while i <= 5:
#     j = 1
#     k = 1
#     while j <= 5 - i:
#         print(" ", end="")
#         j += 1
#     while k <= i:
#         print("* ", end="")
#         k += 1
#     print()
#     i += 1

for i in range(2,101):
    flag = True
    for j in range(2,i):
        if i %j ==0:
            flag=False
            break
    if flag:
        print(i,end=" ")
