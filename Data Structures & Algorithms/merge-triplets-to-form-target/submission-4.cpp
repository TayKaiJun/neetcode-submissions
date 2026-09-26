class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        /*
        observation: if any triplet contain a no. greater than any no. in target, we cannot take it because the value cannot be reduced
        else, we can always take any triplet as any intermediate triplet will increase till we reach target
        */
        bool v[3] = {false, false, false};
        
        for( const auto& curr : triplets ){
            if( curr[0] > target[0] || curr[1] > target[1] || curr[2] > target[2])
                continue;
            for( int i = 0; i < 3; i++ ){
                v[i] |= curr[i] == target[i];
            }
        }
        
        return v[0] && v[1] && v[2];
    }
};
