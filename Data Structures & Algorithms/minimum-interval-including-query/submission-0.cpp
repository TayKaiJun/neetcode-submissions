class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        /*
        core idea - if we sort the queries, each query will have 3 scenarios
        - right < q : all intervals with right < q will no longer be needed for the rest of queries
        - left <= q <= right : candidate intervals
        - q < left : interval irrelevant for now
        */
        vector<pair<int, int>> sortedQueries;

        for (int i = 0; i < queries.size(); i++) {
            sortedQueries.push_back({queries[i], i});
        }
        sort(sortedQueries.begin(), sortedQueries.end());
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<int> output(queries.size());
        // we just need a min-heap prioritizing the length and the interval's right boundary.
        // if we encounter any expired intervals (q > right) then we can pop it
        priority_queue<
            pair<int, int>,
            vector<pair<int, int>>,
            greater<pair<int, int>>
        > smallestLen;
        int intPointer = 0;

        for( auto [q, i] : sortedQueries){
            // add all started intervals
            while( intPointer < intervals.size() && intervals[ intPointer ][0] <= q ){
                int len = intervals[ intPointer ][1] - intervals[ intPointer ][0] + 1;
                smallestLen.emplace( len, intervals[ intPointer ][1] );
                intPointer++;
            }
            // delete expired intervals if they're still in the minheap
            while( !smallestLen.empty() && smallestLen.top().second < q){
                smallestLen.pop();
            }
            
            if( smallestLen.empty() )
                output[i] = -1;
            else
                output[i] = smallestLen.top().first;
        }

        return output;
    }
};
