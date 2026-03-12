from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        
        words = re.findall(r'\w+', paragraph.lower())
        
        count = Counter()
        for w in words:
            if w not in banned:
                count[w] += 1
        
        return count.most_common(1)[0][0]