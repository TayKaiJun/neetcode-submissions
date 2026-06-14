from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cards = Counter(hand)
        n = len(hand)
        if n % groupSize != 0:
            # if n is not divisible by groupSize, no rearrangement is possible
            return False
        
        while cards:
            nums = sorted( cards.keys() )
            lowest = nums[0]
            count = cards[lowest]
            for i in range(groupSize):
                curr = lowest+i
                if cards[curr] < count:
                    return False
                cards[curr] -= count
                if cards[curr] == 0:
                    del cards[curr]
        
        return True