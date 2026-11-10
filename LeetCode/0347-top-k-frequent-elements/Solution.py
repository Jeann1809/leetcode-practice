import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqmap = {}
        for num in nums:
            freqmap[num] = freqmap.get(num, 0)+1

        heap = []
        for num, freq in freqmap.items():
            heap.append((freq,num))
        
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        for freq, num in heap:
            res.append(num)

        return res
        