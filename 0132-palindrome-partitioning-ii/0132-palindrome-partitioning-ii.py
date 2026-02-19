class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # cuts[i] = minimum cuts needed for substring s[:i+1]
        cuts = [i for i in range(n)]
        
        # palindrome table
        is_pal = [[False] * n for _ in range(n)]
        
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_pal[start + 1][end - 1]):
                    is_pal[start][end] = True
                    
                    # If palindrome starts from beginning
                    if start == 0:
                        cuts[end] = 0
                    else:
                        cuts[end] = min(cuts[end], cuts[start - 1] + 1)
        
        return cuts[-1]