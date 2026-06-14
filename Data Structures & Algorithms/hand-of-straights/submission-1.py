from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            # if n is not divisible by groupSize, no rearrangement is possible
            return False
        
        cards = Counter(hand)
        nums = list(cards.keys())
        heapq.heapify(nums)

        while nums:
            lowest = heapq.heappop( nums )
            count = cards[lowest]

            if count == 0:
                continue

            for i in range(groupSize):
                curr = lowest+i
                if cards[curr] < count:
                    return False
                cards[curr] -= count
        
        return True