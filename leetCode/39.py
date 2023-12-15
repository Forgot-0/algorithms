from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    answer = []
    for num in candidates:
        spis = []
        if num > target:
            break
        
        for n in range(target-num):
            pass

candidates = []
target = 0
print(combinationSum(candidates, target))