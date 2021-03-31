numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    min = 0 #index of min val
    for count in range(len(array)-1):
        min = count
        for i in range(count,len(array)):
            if(array[i] < array[min]): #update min index val
                min = i
        # print(array[count],array[min])
        array[count],array[min] = array[min],array[count]

selectionSort(numbers)
print(numbers)