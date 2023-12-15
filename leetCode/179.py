
def largestNumber(nums) -> str:
    min_l = len(str(min(nums)))
    nums = sorted(nums, reverse=True, key=lambda x: tuple([len(str(x))]+[int(i) for i in str(x)[:min_l]]))
    return ''.join((str(s) for s in nums))

n = [111311, 1113]
print(largestNumber(n))