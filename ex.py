def binarysearch(low,high,key):
    if high>low:
        mid=(high+low)//2
        if list1[mid]==key:
            return mid
        elif list1[mid]<key:
            binarysearch(mid+1,high,key)
        elif list1[mid]>key:
            binarysearch(low,mid,key)
    else:
        return -1
list1=[10,20,30,6,18]

index=binarysearch(0,3,90)
if index != -1:
    print("element found in ",list1," at index ",index)
else:
    print("element not found")
