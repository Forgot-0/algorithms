from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        if target-nums[i] in nums:
            if (target-nums[i] == nums[i]) and (nums.count(nums[i]) > 1):
                return [i, (nums[:i]+nums[i+1:]).index(target-nums[i])+1]
            
            if (target-nums[i] != nums[i]):
                return [i, nums.index(target-nums[i])]
    