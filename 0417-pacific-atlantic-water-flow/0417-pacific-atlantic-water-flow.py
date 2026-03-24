class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited):
            visited.add((r, c))
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < m and 0 <= nc < n and 
                    (nr, nc) not in visited and 
                    heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr, nc, visited)
        
        # Pacific (top + left)
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        
        # Atlantic (bottom + right)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)
        
        return list(pacific & atlantic)