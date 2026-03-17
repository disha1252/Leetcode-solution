from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        k -= 1  # convert to 0-based
        result = []
        
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            
            result.append(str(nums[index]))
            nums.pop(index)
            
            k %= fact
        
        return ''.join(result)