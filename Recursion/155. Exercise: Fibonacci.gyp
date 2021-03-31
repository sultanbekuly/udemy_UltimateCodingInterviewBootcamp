def fibanacciIterative(n):#O(n)
    val1 = 0
    val2 = 1 
    for _ in range(n-1):
        val1, val2 = val2, val1 + val2
    return val2

def myfibanacciRecursive(n):
    def myfibanacciRecursive(val1, val2, stopper,counter):
        if(stopper == counter+2):
            return val1 + val2
        else:
            counter += 1
            return myfibanacciRecursive(val2, val1 + val2,stopper,counter)
    return myfibanacciRecursive(0,1,n,0)
    
def fibanacciRecursive(n):#O(2^n) - exponential
    if(n<2):
        print(n)
        return n
    print("#",n-1, n-2)
    return fibanacciRecursive(n-1) + fibanacciRecursive(n-2)

            


# 0 1 1 2 3 5 8 13 21

print(fibanacciIterative(6))
print(fibanacciRecursive(6))
"""3
2 1-1
1-1 0-0
=>2
"""
"""4
3       2
2 1-1
1-1 0-0
        1-1 0
=>3
"""

