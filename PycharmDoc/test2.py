
def binary_search(key,low,high):
    if low > high:
        return
    count = 0
    while low <= high:
        mid=(low+high) //2
        count +=1
        if mid==key:
            print("count= %d" %count)
            return mid
        elif mid <key:
            low = mid
        else:
            high =mid
        return

result = binary_search(1,1,1)
print(result)