arr = [3,1,2,5]
gl=[]
def f(i,a):
    
    if(i>=len(arr)):
        print(a)
        return
    #pick the number
    a.append(arr[i])
    gl.append(a[:])
    f(i+1,a)
    #leave the number
    a.remove(arr[i])
    f(i+1,a)
    gl.append(a[:])
    
    
l=[]
f(0,l)
print(gl)
