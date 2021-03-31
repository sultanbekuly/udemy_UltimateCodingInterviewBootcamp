# Implement a function that reverses a string using iteration...and then recursion!
def reverseString(string):
    if string == "":
        return ""
    return string[-1] + reverseString(string[0:len(string)-1])

string = 'yoyo mastery'
print(reverseString(string))
# should return: 'yretsam oyoy'
