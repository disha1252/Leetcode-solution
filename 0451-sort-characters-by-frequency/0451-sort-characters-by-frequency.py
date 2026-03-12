from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = ""

        for ch, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
            res += ch * freq

        return res