class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        [1,2,3,4]            min = 1, max = 4
        [2,3,3,9,11,12]      min = 2, max = 12
        [1,2,2,3,3,3,4,9,11,12]

        '''
        if len( nums1 ) > len( nums2 ):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        
        n, m = len( nums1 ), len( nums2 )
        i = n // 2
        half = ( n + m ) // 2
        j = half - i

        def getBoundaries( i ):
            '''
            check if partition is valid. 
            - returns 0 if true
            - else return -ve if nums1 partition needs to be shifted left
            - or return +ve if nums1 partition needs to be shifted right
            '''
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == n else nums1[i]
            j = half - i
            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == m else nums2[j]
            # print( f'{left1} i={i} {right1}, {left2} j={j} {right2}' )
            return [left1,right1,left2,right2]
            
        valid = False
        while not valid:
            left1,right1,left2,right2 = getBoundaries(i)
            if left1 > right2:
                i = i // 2
            if right1 < left2:
                i = ( n + i + 1 ) // 2
            valid = True

        left1,right1,left2,right2 = getBoundaries(i)
        if (n+m)%2 == 1:
            return min( right1, right2)
        else:
            return (max(left1, left2) + min(right1, right2)) / 2


        
