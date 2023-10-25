#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

from typing import List

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        nums_len = len(nums)
        if nums_len % 2 == 0:  # even
            idx2 = int(nums_len / 2)
            idx1 = idx2 - 1
            return (nums[idx1] + nums[idx2]) / 2
        else:  # uneven
            idx = int(nums_len / 2)
            return nums[idx]


Solution().findMedianSortedArrays([1, 2], [3, 4])

# @lc code=end
