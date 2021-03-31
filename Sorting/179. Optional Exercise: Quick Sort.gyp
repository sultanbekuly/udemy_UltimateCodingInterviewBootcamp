numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def quicksort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

# print(numbers)
# #Select first and last index as 2nd and 3rd parameters
# print(quicksort(numbers))
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

#Do the Quick sort with ij
# Solution
def quicksort2(array,left,right):
    # ln = len(array)
    if left < right:
        pivot = right
        partitionindex = partition(array, pivot, left, right)

        quicksort2(array, left, partitionindex -1)
        quicksort2(array, partitionindex +1, right)
    return array

def partition(array, pivot, left, right):
    pivotvalue = array[pivot]
    partitionindex = left

    for i in range(left,right):
        if array[i] < pivotvalue:
            swap(array, i, partitionindex)
            partitionindex += 1

    swap(array, right, partitionindex)
    return partitionindex

def swap(array, firstindex, secondindex):
    temp = array[firstindex]
    array[firstindex] = array[secondindex]
    array[secondindex] = temp

# print(numbers)
# #Select first and last index as 2nd and 3rd parameters
# print(quicksort2(numbers,0,len(numbers)-1))


#Do the Quick sort with ij
# Solution
def quicksort_my(array):
    if(len(array) <= 1):
        return array
    
    pivot = array[-1] #last value will be pivot value
    pivot_place = len(array)-1
    i = -1
    # print("pivot",pivot)
    while(i != pivot_place):
        i += 1
        # print(i,array[i],pivot_place)
        if(array[i] > pivot):
            # print(array,i,pivot_place)
            array,i,pivot_place = swap_my(array,i,pivot_place)
            print(array,i,pivot_place)
        
    return quicksort_my(array[:pivot_place])+array[pivot_place:pivot_place+1]+quicksort_my(array[pivot_place+1:])

def swap_my(array,s_i,s_pivot_place):
    if(s_pivot_place-1 == s_i):#just swap
        array[s_i], array[s_pivot_place] = array[s_pivot_place],array[s_i]
        s_pivot_place = s_i #update pivot place
    else:#smart swap
        array[s_i], array[s_pivot_place], array[s_pivot_place-1] = array[s_pivot_place-1],array[s_i],array[s_pivot_place]
        s_pivot_place -= 1 #update pivot place
        s_i -= 1
    return array,s_i,s_pivot_place
        

        
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 99 ]

print(numbers)
#Select first and last index as 2nd and 3rd parameters
print(quicksort_my(numbers))
