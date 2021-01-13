# Binary search on sorted list , reads the list and search for Key Elements and returns its position

lst=[1,3,5,5,11,15,22,34,45,67,69, 75,78,80,86,95,98]
print(len(lst))
key=int(input('Enter Key: '))
# getting low , high & medium index
# based on medium index look for values left or right side of index to get further location

def binsearch(lst):
    low=0
    high = len(lst)   

    while(low <= high):
        medium = (low+high)//2 #getting mid point
        if lst[medium]==key:
            return(medium)
        elif lst[medium] < key:
            low=medium+1            
        else:
            high=medium-1
            
    else:
        return(-1)
            
print("Searching ",key)
idx=binsearch(lst)
if  idx!=-1:
    print('Element {0} available at index'.format(key), idx )
else :
    print('Element {0} not available'.format(key))

