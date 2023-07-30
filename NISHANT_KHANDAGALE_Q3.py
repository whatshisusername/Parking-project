def binarySearch(list1,low,high,key):

    if high>= low:

        mid = low+ (high - low) // 2

        if list1[mid] == key:-
            return mid


        elif list1[mid] > key:
            return binarySearch(list1,low, mid - 1, key)

        else:
            return binarySearch(list1, mid + 1, high, key)

    else:

        return -1



list1=[2, 3, 4, 10, 40]
key=int(input("enter value to search in list:"))
result = binarySearch(list1, 0, len(list1) - 1,key)
if result != -1:
    print("Element is present at index ",result)
else:
    print("Element is not present in list")

