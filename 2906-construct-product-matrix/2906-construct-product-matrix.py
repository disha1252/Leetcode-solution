from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        
        # Step 1: Flatten grid
        arr = [grid[i][j] for i in range(m) for j in range(n)]
        size = m * n
        
        # Step 2: Prefix products
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        
        # Step 3: Suffix products
        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
        
        # Step 4: Build result
        result = [[0] * n for _ in range(m)]
        
        for i in range(size):
            val = (prefix[i] * suffix[i]) % MOD
            result[i // n][i % n] = val
        
        return result