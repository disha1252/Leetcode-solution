class Solution:
    def computeArea(
        self,
        ax1: int, ay1: int, ax2: int, ay2: int,
        bx1: int, by1: int, bx2: int, by2: int
    ) -> int:
        
        # Area of both rectangles
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)
        
        # Overlap dimensions
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        
        # If no overlap
        overlap = 0
        if overlap_width > 0 and overlap_height > 0:
            overlap = overlap_width * overlap_height
        
        return areaA + areaB - overlap