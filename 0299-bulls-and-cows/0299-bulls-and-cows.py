from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        s_count = Counter()
        g_count = Counter()

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_count[s] += 1
                g_count[g] += 1

        cows = 0
        for d in s_count:
            cows += min(s_count[d], g_count[d])

        return f"{bulls}A{cows}B"