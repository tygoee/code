#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

from typing import List, Tuple

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        ns: List[Tuple[str, int]] = [
            ("M", 1000),
            ("D", 500),
            ("C", 100),
            ("L", 50),
            ("X", 10),
            ("V", 5),
            ("I", 1),
        ]

        idx = 0
        c_idx = 0
        total: List[int] = []
        while c_idx < len(s):
            c = s[c_idx]
            if c == ns[idx][0]:
                total.append(ns[idx][1])
            else:
                if not idx >= len(ns) - 1:
                    idx += 1
                else:
                    total[-1] = -total[-1]
                    idx = 0
                continue
            c_idx += 1

        return sum(total)

# @lc code=end
