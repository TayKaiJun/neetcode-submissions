from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        ATTEMPT 2: O(n*m)
        - sort each word O(n * m log m)
        - then create hash map of sorted word->indices - O(n)
        - generate answer from hash map O(n)
        '''
        sortedStrs = [ "".join(sorted(word)) for word in strs ]
        indices = defaultdict(list)
        for i in range(len(sortedStrs)):
            sortedStr = sortedStrs[i]
            indices[ sortedStr ].append( i )
        answer = [ [ strs[i] for i in index ] for index in indices.values() ]
        return answer