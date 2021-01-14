def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        max_index=0
        for j in range(0,n):
            if arr[j]>arr[max_index]:
                max_index=j
        arr[max_index],arr[n-1]=arr[n-1],arr[max_index]
        n=n-1

lst=[int(i) for i in input("Enter numbers :").split(' ')]
selection_sort(lst)
print(lst)
# WorstCase and AverageCase and BestCase : teta(n^2) 
    
 