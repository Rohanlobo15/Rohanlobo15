def mergeSort(li,low,high):
    if(low >= high):
        return
    mid = (low+high)//2
    mergeSort(li,low,mid)
    mergeSort(li,mid+1,high)
    merge(li,low,mid,high)
    

def merge(li,low,mid,high):
    li1 = []
    left = low
    right = mid+1
    while(left<=mid and right <= high):
        if(li[left] <= li[right]):
            li1.append(li[left])
            left += 1
        else:
            li1.append(li[right])
            right += 1
    while(left <= mid):
        li1.append(li[left])
        left += 1
    while(right <= high):
        li1.append(li[right])
        right += 1
    for i in range(len(li1)):
        li[low + i] = li1[i]
    
li = [5,4,2,1,3,6]
mergeSort(li,0,len(li)-1)
print(li)
