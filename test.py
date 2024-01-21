with open(r"C:\Users\mrais\Downloads\24_12476.txt", 'r') as f:
    stroka = f.read()

start = min(stroka.find('ORO'), stroka.find('ROR'))
start += 2
max_v = 0

while start < len(stroka):
    one = stroka.find("ORO", start+2)
    two = stroka.find("ROR", start+2)

    if one == -1 and two == -1:
        stop = len(stroka)-1
    
    elif one == -1:
        stop = two

    elif two == -1:
        stop = one
    
    else:
        stop = min(one, two)

    if stroka[start:stop].count("RO") == 21:
        max_v = max(max_v, stop-start + 1)

    start = stop+2

print(max_v)