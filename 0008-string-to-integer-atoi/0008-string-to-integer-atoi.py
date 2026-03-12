class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        i = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])

            if sign * num >= INT_MAX:
                return INT_MAX
            if sign * num <= INT_MIN:
                return INT_MIN

            i += 1

        return sign * num