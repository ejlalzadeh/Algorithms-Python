def tower_of_hanoi(n,source,destination,intermediate):
    if n==1:
        print(f'Move disk 1 from {source} to {destination}')
        return
    tower_of_hanoi(n-1,source,intermediate,destination)
    print(f'Move disk {n} from {source} to {destination}')
    tower_of_hanoi(n-1,intermediate,destination,source)


n=3
tower_of_hanoi(n,'A','C','B')   