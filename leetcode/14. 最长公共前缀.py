from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos = 0
        res = ""
        while True:
            if len(strs[0]) == pos:
                return res
            for i in range(0, len(strs) - 1):
                if len(strs[i + 1]) == pos or strs[i][pos] != strs[i + 1][pos]:
                    return res
            res += strs[0][pos]
            pos += 1

print(Solution().longestCommonPrefix(["flower","flow","flight"]))

# 可仅比较最大值与最小值的前缀