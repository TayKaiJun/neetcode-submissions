class Solution {
public:
    vector<int> partitionLabels(string s) {
        /*
        since each letter can only appear at most once, we can first find the index of all letters and store their latest index,
        then starting from 0, we process substrings by the following rules:
        - if curr index is > target, it means we completed a substring with all the unique chars, start a new substring
            - calculate length by getting newTarget-currIndex
        - store a target index based on the largest index of the last occurence of the curr letter
            - if target > latest, no op since our current target will already include this
            - if target < latest, we need to move our target = latest 
                - extend curr substring length by latest-target
        - once processed, pop the dict entry of this char

        ^ Version 1 above. We can simplify by maintaining the boundaries and calculating the end when starting a new substring
        */
        unordered_map<char,int> lastIndex;
        for( int i = 0; i < s.length(); i++ ){
            lastIndex[s[i]] = i;
        }

        vector<int> solution;
        int start = 0;
        int end = 0;

        for( int i = 0; i < s.length(); i++ ){
            end = max( end, lastIndex[s[i]] );
            if(i < end)
                continue;
            
            if(i == end){
                solution.push_back( end-start+1 );
                start = i+1;
            }
        }
        return solution;
    }
};
