"""
bigO = log P where P is actual position of element

in a infinite sized sorted array, find an element. 

Works by having a [low, high] interval, then extending that interval while moving it up
to contain the wanted element. Then run binary search. This algo only works with infinite
arrays due to the doubling of the variable "high"
"""

def findPos(array, element):
    low = 0
    high = 1
    while not element < array[high]:
        low = high
        high *= 2
    return binarySearch(array, low, high, element)

def binarySearch(array, low, high, element):
    mid = high / 2
    if array[mid] > element:
        binarySearch(array, low, mid, element)
    elif array[mid] < element:
        binarySearch(array, mid, high, element)
    elif array[mid] == element:
        return mid
    elif low == high:
        return -1

arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170] 
ans = findPos(arr,170)
print(ans)
