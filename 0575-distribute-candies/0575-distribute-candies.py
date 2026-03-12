class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        length=len(set(candyType))
        if len(candyType)//2<=length:
            return len(candyType)//2
        else:
            return length