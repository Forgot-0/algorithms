
def intToRoman(num: int) -> str:
    romans = {
        1: 'I', 
        5: 'V',
        10: 'X', 
        50: 'L', 
        100: 'C', 
        500: 'D', 
        1000: 'M', 
        4:"IV", 
        9:"IX", 
        40:"XL", 
        90:"XC", 
        400:"CD", 
        900: "CM"}

    roman_num = ""
    for i in sorted(romans.keys(), reverse=True):
        if (num//i > 0) and (num//i <= 4):
            roman_num += romans[i]*(num//i)
            num -= i*(num//i)
    return roman_num

roman = 4999
print(intToRoman(roman))