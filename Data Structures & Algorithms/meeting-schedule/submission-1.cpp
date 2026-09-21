/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort( intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b){
            return a.start < b.start;
        });
        int currentEnd = 0;
        for( auto interval : intervals ){
            if( interval.start >= currentEnd ){
                currentEnd = interval.end;
            }
            else
                return false;
        }
        return true;
    }
};
