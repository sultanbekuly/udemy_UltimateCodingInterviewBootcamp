# mergeSortedArrays([0,3,4,31],[4,6,30])
# =>[0,3,4,4,6,30,31]
#merge two sorted arrays
             
def mergeSortedArrays(arr1, arr2):
    #check input:
    if(type(arr1)!=list or type(arr2)!=list
    or arr1 == None  or arr2 == None):
        return "Wrong inputs. There must be two sortes arrays."
    if(len(arr1)==0):
        return arr2
    if(len(arr2)==0):
        return arr1
    
    i=0
    j=0
    final_arr = []
    while i<len(arr1) and j<len(arr2):
        if(arr1[i]<arr2[j]):
            final_arr.append(arr1[i])
            i+=1
        else:
            final_arr.append(arr2[j])
            j+=1
    return final_arr+arr1[i:]+arr2[j:]
print(mergeSortedArrays([0,3,4,31],[4,6,30]))
print(mergeSortedArrays([0,31,31,31],[4,6,30]))
print(mergeSortedArrays([0,3,4,31],[]))
print(mergeSortedArrays([],[4,6,30]))

#creating array with random numbers
from random import randint
randarr1 = sorted([ randint(0,10) for i in range(3)])
randarr2 = sorted([ randint(0,10) for i in range(3)])

print(randarr1, randarr2)
print(mergeSortedArrays(randarr1,randarr2))

print(mergeSortedArrays(1,randarr2))

             
print(type(randarr2))