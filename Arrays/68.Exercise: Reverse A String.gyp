#Create a function that reverse a string:
#'Hi My name is Andrei' should be:
#'ierdnA si eman yM iH'

def reverse(stri):
    if(stri == None or type(stri) != str or len(stri) < 2 ):
        return stri
    str_arr = []
    for i in range(len(stri)-1,-1,-1):
        str_arr.append(stri[i])
    return ''.join(str_arr)

str1 = 'Hi My name is Koska'
print(reverse(str1))
print(reverse(None))
print(reverse('A'))
print(reverse(1))

print(str1[::-1])
