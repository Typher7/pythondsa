import heapq
class KthLargest:
    def __init__(self, k, numbers):
        self.minHeap, self.k = heapq.heapify(numbers)

    def add(self, val):
        pass