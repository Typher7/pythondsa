import heapq

def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [ -s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first-second)
        stones.append(0)
        return abs(stones[0])