
def reverse(x):
    str_x = str(x)
    if '-' in str_x:
        res = int('-' + str_x[1:][::-1])
    else:
        res = int(str_x[::-1])

    if len(bin(int(res))[2:].replace('b', '')) > 32:
        return 0 
     
    return res

print(reverse(-2147483412))
print((bin(-2147483412)[2:]))