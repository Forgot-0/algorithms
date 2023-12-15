from typing import List


def plusOne(digits: List[int]) -> List[int]:
    numbers = int(str(digits).replace("[", "").replace("]", "").replace(",", "").replace(" ", ""))+1

    return [int(i) for i in str(numbers)]

d = [1,2,3,4]
print(plusOne(d))

