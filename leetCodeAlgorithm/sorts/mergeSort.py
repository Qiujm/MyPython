def partition(lyst, left, right):
    middle = (left+right) //2
    piv = lyst[middle]
    lyst[right]=piv
    boundary=left
    for index in range(left,right):
        if lyst[index] <piv:
            # lyst[index],lyst[boundary] = lyst[boundary],lyst[index]
            swap(lyst,index,boundary)
            boundary +=1
    swap(lyst,right,boundary)
    return boundary



def quickSortHelp(lyst, left, right):
    if left<right:
        pivLocation = partition(lyst,left,right)
        quickSortHelp(lyst,left,pivLocation-1)
        quickSortHelp(lyst,pivLocation+1,right)


def quickSort(lyst):
    quickSortHelp(lyst,0,len(lyst)-1)

def swap(lyst,a,b):
    lyst[a].lyst[b]=lyst[b],lyst[a]