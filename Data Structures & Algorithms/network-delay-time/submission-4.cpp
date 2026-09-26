class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        //Dijkstra's
        unordered_set<int> visited;
        int time = 0;
        // store node no. to their edges (index to the times vector)
        unordered_map<int, vector<int>> graph;
        
        for( int i = 0; i < times.size(); i++ ){
            graph[times[i][0]].push_back(i);
        }
        priority_queue< pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;

        visited.insert(k);
        for( int i : graph[k] ){
            int next = times[i][1];
            int cost = times[i][2];
            minHeap.emplace(cost,next);
        }

        while(!minHeap.empty()){
            auto [cost, node] = minHeap.top();
            minHeap.pop();
            if(visited.contains(node))
                continue;

            visited.insert(node);

            if(visited.size()==n)
                return cost;

            for( int i : graph[node] ){
                int next = times[i][1];
                if( !visited.contains(next) )
                    minHeap.emplace(cost+times[i][2],next);
            }
        }

        return -1;
        
    }
};
