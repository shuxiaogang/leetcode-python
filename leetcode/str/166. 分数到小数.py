class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 符号
        sym = '-' if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        # 整数
        integer = abs(numerator) // (denominator)
        if numerator % denominator == 0: return sym + str(integer)
        res = [sym, str(integer), '.']
        pos_dict = {}
        while (numerator := (numerator % denominator) * 10) != 0 and numerator not in pos_dict:
            pos_dict[numerator] = len(res)
            res.append(str(numerator // denominator))
        # 循环
        if numerator in pos_dict:
            res.insert(pos_dict[numerator], '(')
            res.append(")")
        return "".join(res)
