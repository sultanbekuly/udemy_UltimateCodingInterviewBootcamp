numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(array):
    counter = 0
    while (counter != len(array)-1):
        # print("#",counter)
        for i in range(len(array)-counter-1):
            # print(i,i+1,array[i], array[i+1])
            if(array[i] > array[i+1]):#do swap
                array[i],array[i+1] = array[i+1],array[i]
        counter += 1
        # print(array)
    return array
    
numbers = bubbleSort(numbers)
print(numbers)