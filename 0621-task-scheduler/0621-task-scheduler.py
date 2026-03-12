from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)

        maxFreq = max(count.values())
        maxCount = list(count.values()).count(maxFreq)

        formula = (maxFreq - 1) * (n + 1) + maxCount

        return max(len(tasks), formula)