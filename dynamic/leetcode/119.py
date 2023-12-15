from typing import List



def factorial(n, k=2):
    ans = 1
    for i in range(k, n+1):
        ans *= i
        
    return ans


def getRow(rowIndex: int) -> List[int]:
    ans = [1]
    for i in range(1, rowIndex//2+1):
        ans.append(factorial(rowIndex, rowIndex-i+1)//factorial(i))

    ans += ans[::-1]

    if rowIndex%2:
        return ans

    ans.pop(rowIndex//2)
    return ans

print(getRow(4))