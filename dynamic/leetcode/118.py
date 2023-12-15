from typing import List


def generate(numRows: int) -> List[List[int]]:
    beging = [[1], [1, 1]][:numRows]

    for n in range(1, numRows-1):
        m = [1]
        for i in range(len(beging[n])-1):
            m.append(beging[n][i] + beging[n][i+1])
    
        m.append(1)
        beging.append(m)

    return (beging)

print(generate(11))