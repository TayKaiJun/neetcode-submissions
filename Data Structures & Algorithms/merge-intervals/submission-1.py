class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = max([ i[1] for i in intervals ])
        intervals.sort(key=lambda x: (x[0],-x[1]) )
        members = [0] * (n+1)
        groupBoundaries = {}
        print(intervals)

        '''
        cases:
            1: not within any boundary = get next available group number in groupBoundaries & mark all members
            2: start OR end are within boundaries = extend them & update groupBoundaries
            3: start AND end are within boundaries = connect the end to the start & remove the end's group
                3.1: start AND end are within SAME boundary = no-op, it's a subset of an existing interval
        '''
        def updateMembership(start, end, group):
            for i in range(start,end+1):
                if members[i] != 0 and members[i] != group and members[i] in groupBoundaries:
                    del groupBoundaries[ members[i]]
                members[i] = group

        for interval in intervals:
            start,end = interval
            frontGroup = members[ start ]
            backGroup = members[ end ] 
            if frontGroup != 0:
                if backGroup != 0:
                    if frontGroup == backGroup:
                        # case 3.1
                        continue
                    # case 3 (extends frontGroup)
                    newEnd = groupBoundaries[backGroup][1]
                    updateMembership( start, newEnd, frontGroup )
                    groupBoundaries[frontGroup][1] = newEnd
                    continue
                
                else:
                    # case 2 (only start overlaps - extend frontGroup)
                    updateMembership( groupBoundaries[frontGroup][1], end, frontGroup )
                    groupBoundaries[frontGroup][1] = end
                    continue
            
            if backGroup != 0:
                # case 2 (only end overlaps - extend backGroup)
                updateMembership( start, groupBoundaries[backGroup][0], backGroup )
                groupBoundaries[backGroup][0] = start
                continue

            # case 1: no overlap exists (find a new group number)
            group = 1
            while group in groupBoundaries:
                group += 1 
            updateMembership( start, end, group)
            groupBoundaries[group] = [start, end]
            
        return [ i for i in groupBoundaries.values() ]
