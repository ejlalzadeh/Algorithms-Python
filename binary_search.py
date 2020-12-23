inp_str = input("Enter numbers:")
target= int (input("Enter your target number:"))
lst=[int(i) for i in inp_str.split(' ') ]

def binary_search(lst,low,high,target):
    if low <high:
        mid = (low +high)//2
        if lst[mid]==target:
            return mid+1
        elif lst[mid]>target:
            return binary_search(lst,0,mid-1,target)
        elif lst[mid]<target:
            return binary_search(lst,mid+1,high,target)
    else : 
        return "Not Found"        



mid = binary_search(lst,0,len(lst)-1,target)
print(mid)