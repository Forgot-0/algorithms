from typing import List



def letterCombinations(digits: str) -> List[str]:
    slovar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    
    if len(digits) == 1: return list(slovar[digits[0]])
    if len(digits) == 0: return []
    new_spisok = letterCombinations(digits[:-1])
    last = list(slovar[digits[-1]])
    spisok = [s1+s2 for s1 in new_spisok for s2 in last]
    
    return spisok

d = "234"

print(letterCombinations(d))
