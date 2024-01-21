

from typing import List


def numSpecial(mat: List[List[int]]) -> int:
    stolb = [[mat[j][i] for j in range(len(mat[0]))] for i in range(len(mat))]
    count = 0
    for i in range(len(mat)):
        if mat[i].count(1) == 1 and stolb[mat[i].index(1)].count(1) == 1:
            count += 1

    return count



print(numSpecial([[1,0,0],[0,0,1],[1,0,0]]))