from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ### Attempt 1: O(n^2) solution
        answer = []

        n = len(strs)
        for i in range(n):
            word = strs[i]
            # if it's -1, it's a word we already grouped
            if word == -1:
                continue
            
            group = [ word ]
            wordCount = Counter( word )

            for j in range(i+1, n):
                groupWord = strs[j]
                if groupWord == -1:
                    continue
                groupWordCount = Counter( groupWord )
                # if this word matches, add to group and clear this str
                if wordCount == groupWordCount:
                    group.append( groupWord )
                    strs[j] = -1
            
            answer.append( group )
        return answer