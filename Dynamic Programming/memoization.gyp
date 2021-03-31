def memoizedAddTo80():
    cache = {}
    def memoized(n):
        if(n in cache):
            return cache[n]
        else:
            print("long time")
            cache[n] = n+80
            return cache[n]
    return memoized

memo = memoizedAddTo80()

print(memo(7))
print(memo(7))

