class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        since each letter can only appear at most once, we can first find the index of all letters and store their latest index,
        then starting from 0, we process substrings by the following rules:
        - if curr index is > target, it means we completed a substring with all the unique chars, start a new substring
            - calculate length by getting newTarget-currIndex
        - store a target index based on the largest index of the last occurence of the curr letter
            - if target > latest, no op since our current target will already include this
            - if target < latest, we need to move our target = latest 
                - extend curr substring length by latest-target
        - once processed, pop the dict entry of this char
        '''
        lastIndex = {}
        for i,c in enumerate(s):
            lastIndex[c]=i

        target = -1
        sol = []

        for i,c in enumerate(s):
            if not lastIndex:
                # all letters were processed, we can return early
                break

            if c not in lastIndex:
                # if entry dont exist means we processed this letter before
                continue
            
            # processing this letter, gotta remove it from the dict
            last = lastIndex[c]
            del lastIndex[c]
            
            if i > target:
                # case: start new substring
                sol.append(last-target)
                target = last
                continue
            
            if last > target:
                # case: need to extend the curr substring as a letter it contain has a later occurence
                sol[-1] = sol[-1] + last-target
                target = last
            # case target > last: no op, our current substring already include the last occurence
        
        return sol


