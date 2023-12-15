from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    spisok = set()

    for i in range(len(nums)):
        for n in range(i+1, len(nums)):
            find_num = 0-(nums[n]+nums[i])
            if find_num in nums:
                ind = nums.index(find_num)
                if ind != n and ind != i:
                    spisok.add(tuple(([find_num, nums[n], nums[i]])))
    return spisok


#nums = [0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]#[0,0,0]#[-1,0,1,2,-1,-4]
nums = [-1, 0, 1, 2, -1, -4]
#nums = [0,0,0,0]
#1- 2+
#2- 1+
print(threeSum(nums))
#Runtime: 1673 ms