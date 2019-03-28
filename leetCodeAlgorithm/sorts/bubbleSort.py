
def bubbleSort(lyst):
    """bubble sort"""
    for i in range(len(lyst)-1,0,-1):

        for j in range(0,i):
            if lyst[j] >lyst[j+1]:
                lyst[j],lyst[j+1] = lyst[j+1],lyst[j]

lyst2=[2]
lyst= [3,1,7,4,8,333,55,76,2]
bubbleSort(lyst2)
print(lyst2)
# for i in range(5,0,-1):
#     print(i)