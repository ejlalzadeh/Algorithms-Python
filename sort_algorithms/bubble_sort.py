inp_str = input("Enter numbers:")
lst=[int(i) for i in inp_str.split(' ') ]

def bubble_sort(lst):
    for i in range(0,len(lst)-1):
        for j in range(0,len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]


bubble_sort(lst)
print(lst)      

# WorstCase and AverageCase and BestCase : θ(n^2) 