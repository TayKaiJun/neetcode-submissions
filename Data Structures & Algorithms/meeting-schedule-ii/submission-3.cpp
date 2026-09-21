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
    int minMeetingRooms(vector<Interval>& intervals) {
        if( intervals.empty() )
            return 0;

        sort( intervals.begin(), intervals.end(), []( const Interval& a, const Interval& b){
            if(a.start == b.start){
                return a.end < b.end;
            }
            return a.start < b.start;
        });

        int numRoom = 1;
        // use a minheap to track the next available time
        priority_queue< int, vector<int>, std::greater<int>> nextAvail;
        nextAvail.push(0);

        for( auto interval : intervals ){
            if( interval.start >= nextAvail.top()){
                nextAvail.pop();
            }
            else{
                numRoom += 1;
            }
            nextAvail.push(interval.end);
        }
        return numRoom;
    }
};
