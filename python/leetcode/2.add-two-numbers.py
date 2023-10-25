#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional, Union


class ListNode:
    def __init__(self, val: int = 0, next: Union["ListNode", None] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = 0
        nums: list[int] = []

        while True:
            if l1 is not None or l2 is not None:
                addition = (l1.val if l1 is not None else 0) + \
                    (l2.val if l2 is not None else 0) + stack
                stack = 0
                if addition >= 10:
                    stack += addition // 10
                    addition = addition % 10
                nums.insert(0, addition)
                l1 = l1.next if l1 is not None else None
                l2 = l2.next if l2 is not None else None

            elif l1 is None and l2 is None:
                break

        if stack > 0:
            nums.insert(0, stack)

        result = ListNode(nums[0])
        for i in nums[1:]:
            result = ListNode(i, result)

        return result

# @lc code=end
