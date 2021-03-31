# //Google Question
# //Given an array = [2,5,1,2,3,5,1,2,4]:
# //It should return 2

# //Given an array = [2,1,1,2,3,5,1,2,4]:
# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return undefined

# function firstRecurringCharacter(input) 
# }

# //Bonus... What if we had this:
# // [2,5,5,2,3,5,1,2,4]
# // return 5 because the pairs are before 2,2

def firstRecurringCharacter(input):
    #check input
    if(type(input)!=list):
        return "Wrong input. It must be array."
    if(len(input) <2 ):
        return None
    #check every item is type int during loop
    dict_input = {}
    for i in input:
        if(type(i)!=int):
            return "Wrong input.(array item)"
        if(dict_input.get(i)==True):
            return i
        else:
            dict_input[i]= True
    return None
    #O(n) - time complexity

print(firstRecurringCharacter([2,1,1,2,3,5,1,2,4]))
print(firstRecurringCharacter([2,5,1,2,3,5,1,2,4]))
print(firstRecurringCharacter([2,3,4,5]))
print(firstRecurringCharacter([2,5,5,2,3,5,1,2,4]))

print('test:')
print(firstRecurringCharacter( []))
print(firstRecurringCharacter( [1]))
print(firstRecurringCharacter( "array"))
print(firstRecurringCharacter( [1,2,"1",2] ))

