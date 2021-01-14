def insertion_sort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while  j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

lst=[4,7,19,8,6,13,1]
insertion_sort(lst,len(lst))
print(lst)
            
# Worst Case and Average Case : teta(n^2)
# Best Case : teta(n)