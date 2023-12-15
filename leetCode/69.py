
def mySqrt(x: int) -> int:
    first = 1
    number = int(x)
    for i in range(50):
        number = (first+x/first)/2
        first = number
    return int(number)



num = 998001
print(mySqrt(num))


