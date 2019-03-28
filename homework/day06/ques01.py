# for循环输出1-100之间的所有质数。
import math
for num in range(2,101):
    div=2
    flag=True
    while div*div <= num:
        if  num % div==0:
            flag=False
            break
        div+=1
    if flag:
        print(num,end=" ")
print()

for num in range(2,101):
    # for div in range(2,num):
    for div in range(2,1+int(math.sqrt(num))):
        if num % div==0:
            break
    else:
        print(num,end=" ")

# a=20
# for i in range(a):
#     print(i)
#     a-=1
