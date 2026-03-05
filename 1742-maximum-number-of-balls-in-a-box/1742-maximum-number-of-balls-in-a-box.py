class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}

        for num in range(lowLimit, highLimit + 1):
            digit_sum = sum(map(int, str(num)))
            
            if digit_sum in boxes:
                boxes[digit_sum] += 1
            else:
                boxes[digit_sum] = 1

        return max(boxes.values())