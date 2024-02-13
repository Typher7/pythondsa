import heapq
class KthLargest:
    def __init__(self, k, numbers):
        self.minHeap, self.k = numbers, k
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


    def add(self, val):
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        #return kth largest after popping
        return self.minHeap[0]
