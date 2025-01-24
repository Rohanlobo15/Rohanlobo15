arr = [2,3,4,1,5,6,8]
s =8
def printsumequalsk(i,a,sm):
    if sm==s:
        print(a)
        return
    
    if i>=len(arr):
        return
    
    
    a.append(arr[i])
    sm+=arr[i]
    printsumequalsk(i+1,a,sm)
    a.remove(arr[i])
    sm-=arr[i]
    printsumequalsk(i+1,a,sm)

printsumequalsk(0,[],0)
