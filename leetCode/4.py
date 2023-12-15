from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    sum_s = sorted(nums1+nums2)
    len_s = len(sum_s)
    if len_s%2==0:return (sum_s[len_s//2]+sum_s[len_s//2-1])/2
    return sum_s[len_s//2]

