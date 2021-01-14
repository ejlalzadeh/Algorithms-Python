def merge_sort(arr,first,last):
    if last-first>0:
        mid=(first+last)//2
        merge_sort(arr,first,mid)
        merge_sort(arr,mid+1,last)
        merge(arr,first,mid,last)
        
def merge(arr,first,mid,last):
    n1=mid-first+1
    n2=last-mid
    L,R=[None]*n1,[None]*n2
    for i in range(0,n1):
        L[i]=arr[i+first]
    for j in range(0,n2):
        R[j]=arr[mid+1+j]
    i=j=0
    k=0
    #merging
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k+first]=L[i]
            i+=1
        else:
            arr[k+first]=R[j]
            j+=1
        k+=1
    while i<n1:
        arr[k+first]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k+first]=R[j]
        j+=1
        k+=1

lst=[70,10,4,12,2,32,65]
merge_sort(lst,0,len(lst)-1)
print(lst)





# T(n)=2T(n/2)+θ(n) Note : θ(n) is TimeComplexity of merge function
# TimeComplexity = θ(nLogn)