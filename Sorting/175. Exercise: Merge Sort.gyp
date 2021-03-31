import math

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def mergeSort (array):
    if (len(array) == 1):
        return array
  
    # Split Array in into right and left
    middle = int(math.floor(len(array)/2))
    # print(half_of_array, type(half_of_array))
    left = array[:middle]
    right = array[middle:]
    print(left, right)

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    pointerL = 0
    pointerR = 0
    array = []
    while(pointerL!=len(left) and pointerR!=len(right)):
        if(left[pointerL]<right[pointerR]):
            array.append(left[pointerL])
            pointerL += 1
        else:
            array.append(right[pointerR])
            pointerR += 1
    array = array + left[pointerL:] + right[pointerR:]
    print(array)
    return array

# print(numbers[0:2])

answer = mergeSort(numbers)
print(answer)