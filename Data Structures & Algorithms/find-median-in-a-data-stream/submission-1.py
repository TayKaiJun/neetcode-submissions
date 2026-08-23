class MedianFinder:

    def __init__(self):
        self.bottom = [] # max heap of lowest half numbers
        self.top = [] # min heap of top half numbers

    def addNum(self, num: int) -> None:
        # print('addingNum', num)
        # Edge case: first element in the stream
        if not self.bottom:
            self.bottom.append(-num)
            return
        
        '''
        Regular case:
        - if new number is larger than the biggest number in bottom half,
           - if len(bottom)-len(top)==1, then add to top
           - if len(bottom) == len(top), then move the smallest in top to bottom and add this to top
        '''
        biggestBottom = -self.bottom[0]
        # print('biggestBottom', biggestBottom)
        odd = (len(self.bottom)+len(self.top)+1)%2
        if num <= biggestBottom:
            if odd:
                heapq.heappush( self.bottom, -num )
            else:
                heapq.heappushpop( self.bottom, -num )
                heapq.heappush( self.top, biggestBottom )
        else:
            if odd:
                # we maintain bottom to be the one holding 1 extra element, 
                # so move the smallestTop into Bottom
                smallestTop = heapq.heappushpop( self.top, num )
                heapq.heappush( self.bottom, -smallestTop )
            else:
                heapq.heappush( self.top, num )
        
        # print(self.bottom)
        # print(self.top)

    def findMedian(self) -> float:
        a = -self.bottom[0]
        if self.top and len(self.top)==len(self.bottom):
            # even length list
            b = self.top[0]
            return (a+b)/2
        return a

        