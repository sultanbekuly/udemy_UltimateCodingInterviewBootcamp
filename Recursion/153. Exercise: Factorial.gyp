def findFactorialRecursive(number):
    if(number == 1):
        return 1
    else:
        return number * findFactorialRecursive(number-1)

def findFactorialIterative(number):
    res = 1
    for i in range(2,number+1):
        res *= i
    return res


print(findFactorialRecursive(6))
print(findFactorialIterative(7))
#1 2 6 24 120 720 5040