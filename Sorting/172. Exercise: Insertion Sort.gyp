numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(array):
    for i in range(1,len(array)):
        # print("#i",i,array[i])
        for j in range(i-1,-1,-1):
            # print("j",j,array[j])
            if(array[j]>array[j+1]):#swap
                # print("swap", array)
                array[j], array[j+1] = array[j+1], array[j]
            else:#stop
                break
        # print(array)
    return

insertionSort(numbers)
print(numbers)