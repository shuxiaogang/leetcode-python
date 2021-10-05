class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # 数学，或者矩阵
        rows = [[] for i in range(numRows)]
        ri = -1
        down = True
        for c in s:
            if ri == 0:
                down = True
            elif ri == numRows - 1:
                down = False
            ri += 1 if down else -1
            rows[ri].append(c)
        res = ""
        for s in rows:
            res = res + "".join(s)
        return res


print(Solution().convert("AB", 1))
