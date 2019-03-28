# 使用循环手工输入5个整数，并将其存入列表，使用二种方法求出最大值，和最小值。
import random

lyst = []
for i in range(5):
    lyst.append(random.randint(10,20))

print(lyst)
lyst.sort()
print(lyst)
print(lyst[len(lyst) - 1])
