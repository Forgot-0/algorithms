
def romanToInt(s: str) -> int:
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    numbers = 0
    for i in range(1, len(s)):
        if roman[s[i-1]] < roman[s[i]]:
            numbers -= roman[s[i-1]]
        else:
            numbers += roman[s[i-1]]
    numbers += roman[s[-1]]
    return numbers

print(romanToInt('MMMCMXCVIII'))