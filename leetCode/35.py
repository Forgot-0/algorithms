from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    
    if target in nums: return nums.index(target)
    nums1 = [i for i in nums if i <= target]
    return len(nums1)
        

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))