class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_s = s.replace('-', "")
        pos = len(new_s) % k
        res = []
        if pos != 0:
            res.append(new_s[:pos])
        while pos != len(new_s):
            res.append(new_s[pos:pos + k])
            pos += k
        return "-".join(res).upper()
