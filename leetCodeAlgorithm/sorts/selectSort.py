
def selectSort(lyst):
    """selected sort"""
    if lyst in (None,''):
        return
    for i in range(len(lyst)-1):
        min = i
        for j in range(i+1,len(lyst)):
            if lyst[j]<lyst[min]:
                min = j
        if lyst[i] !=lyst[min]:
            lyst[i],lyst[min] = lyst[min],lyst[i]


lyst2=[2]
lyst= [3,1,7,4,8,333,55,76,2]
selectSort(lyst)
print(lyst)
