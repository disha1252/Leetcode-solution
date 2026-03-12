import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        heap = []

        for j in range(1, n):
            heapq.heappush(heap, (arr[0]/arr[j], 0, j))

        for _ in range(k-1):
            _, i, j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap, (arr[i+1]/arr[j], i+1, j))

        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]