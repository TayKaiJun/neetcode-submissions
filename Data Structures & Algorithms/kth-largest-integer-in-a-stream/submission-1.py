import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = nums
        self.k = k
        heapq.heapify( self.maxHeap )
        while len(self.maxHeap) > k:
            heapq.heappop( self.maxHeap )

    def add(self, val: int) -> int:
        heapq.heappush( self.maxHeap, val )
        if len(self.maxHeap) > self.k:
            heapq.heappop( self.maxHeap )
        return self.maxHeap[0]

        
