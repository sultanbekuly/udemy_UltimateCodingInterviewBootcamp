#0 1 1 2 3 5 8 13 21 34 55 89 144 233 ...

calculations = {0:0,1:0,2:0}
calc = 0
def fibSlow(n):
    calculations[0] += 1
    global calc
    calc += 1
    if(n<2):
        return n
    return fibSlow(n-1) + fibSlow(n-2)


def fibFast():
    cache = {}
    def memoized(n):
        calculations[1] += 1
        if(n in cache):
            return cache[n]
        else:
            if(n<2):
                return n
            cache[n] = memoized(n-1) + memoized(n-2)
            return cache [n]
    return memoized

def fibFast2(n):
    answer = [0,1]
    for i in range(2,n+1):
        calculations[2] += 1
        answer.append(answer[i-2]+answer[i-1])
    return answer[-1]

myfibFast = fibFast()

print(fibSlow(10))
print(myfibFast(10))
print(fibFast2(10))
print(calculations)
print(calc)