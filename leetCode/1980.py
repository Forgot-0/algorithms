



def findDifferentBinaryString(nums) -> str:
    n = len(nums)
    for i in range(int('1'+'0'*(n-1), 2), int('1'*n, 2)):
        if bin(i)[2:] not in nums:
            return bin(i)[2:]
    return '0'*n